#!/usr/bin/env python3
"""Validate non-skippable evidence for a reference-driven identity-skill run."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import struct
import sys
import tempfile
import zlib
from pathlib import Path


VIEWPORTS = ("desktop", "ultrawide", "mobile")
GATES = (
    "visual_meaning",
    "hierarchy",
    "personal_evidence",
    "composition",
    "typography",
    "asset_crop",
    "overlap",
    "responsive",
    "reference_fidelity",
)
LOCK_PARTS = {"locked", "reference-lock", "original-lock"}
REVIEW_MODES = {"fresh-thread", "independent", "self-blind"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("not a PNG with a valid IHDR header")
    return struct.unpack(">II", header[16:24])


def resolve_inside(root: Path, value: object, label: str, errors: list[str]) -> Path | None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label}: expected a non-empty relative path")
        return None
    candidate = (root / value).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        errors.append(f"{label}: path escapes project root: {value}")
        return None
    return candidate


def require_text_artifact(
    root: Path, value: object, label: str, section_ids: list[str], errors: list[str]
) -> None:
    path = resolve_inside(root, value, label, errors)
    if path is None:
        return
    if not path.is_file() or path.stat().st_size == 0:
        errors.append(f"{label}: missing or empty file: {path}")
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    for section_id in section_ids:
        marker = re.compile(
            rf"<!--\s*identity-section:{re.escape(section_id)}\s+status=pass\s*-->",
            re.IGNORECASE,
        )
        if marker.search(text) is None:
            errors.append(f"{label}: missing pass marker for section '{section_id}'")


def validate(project_root: Path, manifest_rel: str = "docs/identity-evidence.json") -> list[str]:
    root = project_root.resolve()
    errors: list[str] = []
    manifest_path = resolve_inside(root, manifest_rel, "manifest", errors)
    if manifest_path is None:
        return errors
    if not manifest_path.is_file():
        return [f"manifest: missing file: {manifest_path}"]

    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"manifest: cannot read valid JSON: {exc}"]

    if not isinstance(data, dict):
        return ["manifest: top level must be an object"]
    if data.get("schema_version") != 1:
        errors.append("manifest: schema_version must be 1")
    lock_version = data.get("reference_lock_version")
    if not isinstance(lock_version, str) or not lock_version.strip():
        errors.append("manifest: reference_lock_version must be non-empty")
        lock_version = None
    if data.get("source_strategy_locked") is not True:
        errors.append("manifest: source_strategy_locked must be true")
    if data.get("review_scope") != "all_sections":
        errors.append("manifest: review_scope must be 'all_sections'")
    if data.get("fresh_review_mode") not in REVIEW_MODES:
        errors.append("manifest: fresh_review_mode must be fresh-thread, independent, or self-blind")
    if data.get("final_status") != "pass":
        errors.append("manifest: final_status must be 'pass'")

    viewports = data.get("viewports")
    if not isinstance(viewports, dict):
        viewports = {}
        errors.append("manifest: viewports must be an object")
    for name in VIEWPORTS:
        viewport = viewports.get(name)
        if not isinstance(viewport, dict):
            errors.append(f"viewports.{name}: missing object")
            continue
        for axis in ("width", "height"):
            if not isinstance(viewport.get(axis), int) or viewport[axis] <= 0:
                errors.append(f"viewports.{name}.{axis}: expected a positive integer")

    sections = data.get("sections")
    if not isinstance(sections, list) or not sections:
        return errors + ["manifest: sections must be a non-empty array"]

    section_ids: list[str] = []
    declared_section_ids = {
        section.get("id")
        for section in sections
        if isinstance(section, dict) and isinstance(section.get("id"), str) and section["id"].strip()
    }
    seen_ids: set[str] = set()
    for index, section in enumerate(sections):
        label = f"sections[{index}]"
        if not isinstance(section, dict):
            errors.append(f"{label}: expected an object")
            continue
        section_id = section.get("id")
        if not isinstance(section_id, str) or not section_id.strip():
            errors.append(f"{label}.id: expected a non-empty string")
            continue
        if section_id in seen_ids:
            errors.append(f"{label}.id: duplicate section id '{section_id}'")
        seen_ids.add(section_id)
        section_ids.append(section_id)
        prefix = f"section '{section_id}'"

        reference = section.get("reference")
        reference_path: Path | None = None
        reference_digest: str | None = None
        if not isinstance(reference, dict):
            errors.append(f"{prefix}: reference must be an object")
        else:
            reference_value = reference.get("path")
            reference_path = resolve_inside(root, reference_value, f"{prefix}.reference.path", errors)
            parts = Path(reference_value).parts if isinstance(reference_value, str) else ()
            locked_versions = {
                parts[index + 1]
                for index, part in enumerate(parts[:-1])
                if part in LOCK_PARTS
            }
            if not locked_versions:
                errors.append(f"{prefix}: reference path must live under a locked version directory")
            elif lock_version is not None and lock_version not in locked_versions:
                errors.append(
                    f"{prefix}: reference path does not use manifest lock version '{lock_version}'"
                )
            expected_digest = reference.get("sha256")
            if not isinstance(expected_digest, str) or len(expected_digest) != 64:
                errors.append(f"{prefix}.reference.sha256: expected a 64-character SHA-256")
            if reference_path is not None:
                if not reference_path.is_file():
                    errors.append(f"{prefix}: missing reference: {reference_path}")
                else:
                    reference_digest = sha256(reference_path)
                    if reference_digest != expected_digest:
                        errors.append(f"{prefix}: reference SHA-256 mismatch; lock was changed")

        contract = resolve_inside(root, section.get("render_contract"), f"{prefix}.render_contract", errors)
        if contract is not None and (not contract.is_file() or contract.stat().st_size == 0):
            errors.append(f"{prefix}: missing or empty render contract: {contract}")

        topology = section.get("topology")
        if not isinstance(topology, dict):
            errors.append(f"{prefix}: topology must be an object")
        else:
            kind = topology.get("kind")
            shared_with = topology.get("shared_with")
            reason = topology.get("reason")
            if kind not in {"section-specific", "shared"}:
                errors.append(f"{prefix}.topology.kind: use 'section-specific' or 'shared'")
            if not isinstance(shared_with, list):
                errors.append(f"{prefix}.topology.shared_with: expected an array")
            elif kind == "shared" and not shared_with:
                errors.append(f"{prefix}: shared topology must name at least one section")
            elif kind == "shared":
                for shared_id in shared_with:
                    if not isinstance(shared_id, str) or not shared_id.strip():
                        errors.append(f"{prefix}.topology.shared_with: expected non-empty section ids")
                    elif shared_id == section_id:
                        errors.append(f"{prefix}: shared topology cannot reference itself")
                    elif shared_id not in declared_section_ids:
                        errors.append(f"{prefix}: shared topology references unknown section '{shared_id}'")
                if not isinstance(topology.get("shared_geometry"), str) or not topology["shared_geometry"].strip():
                    errors.append(f"{prefix}.topology.shared_geometry: expected a non-empty description")
                if not isinstance(topology.get("responsive_behavior"), str) or not topology[
                    "responsive_behavior"
                ].strip():
                    errors.append(f"{prefix}.topology.responsive_behavior: expected a non-empty description")
            if not isinstance(reason, str) or not reason.strip():
                errors.append(f"{prefix}.topology.reason: expected a non-empty reason")

        captures = section.get("captures")
        if not isinstance(captures, dict):
            captures = {}
            errors.append(f"{prefix}: captures must be an object")
        for viewport_name in VIEWPORTS:
            capture = resolve_inside(
                root, captures.get(viewport_name), f"{prefix}.captures.{viewport_name}", errors
            )
            if capture is None:
                continue
            if not capture.is_file() or capture.stat().st_size == 0:
                errors.append(f"{prefix}: missing capture for {viewport_name}: {capture}")
                continue
            try:
                actual = png_dimensions(capture)
            except (OSError, ValueError) as exc:
                errors.append(f"{prefix}: invalid {viewport_name} capture: {exc}")
                continue
            viewport = viewports.get(viewport_name, {})
            expected = (viewport.get("width"), viewport.get("height"))
            if all(isinstance(value, int) for value in expected) and actual != expected:
                errors.append(
                    f"{prefix}: {viewport_name} capture is {actual[0]}x{actual[1]}, expected {expected[0]}x{expected[1]}"
                )
            if reference_digest is not None and sha256(capture) == reference_digest:
                errors.append(f"{prefix}: {viewport_name} capture is a copy of the locked reference")

        gates = section.get("gates")
        if not isinstance(gates, dict):
            gates = {}
            errors.append(f"{prefix}: gates must be an object")
        for gate in GATES:
            if gates.get(gate) != "pass":
                errors.append(f"{prefix}.gates.{gate}: must be 'pass'")
        if section.get("status") != "pass":
            errors.append(f"{prefix}.status: must be 'pass'")

    require_text_artifact(root, data.get("fidelity_ledger"), "fidelity_ledger", section_ids, errors)
    require_text_artifact(root, data.get("fresh_review"), "fresh_review", section_ids, errors)
    return errors


def _png_chunk(kind: bytes, payload: bytes) -> bytes:
    return struct.pack(">I", len(payload)) + kind + payload + struct.pack(">I", zlib.crc32(kind + payload) & 0xFFFFFFFF)


def _write_png(path: Path, width: int, height: int, rgb: tuple[int, int, int]) -> None:
    row = bytes(rgb) * width
    raw = b"".join(b"\x00" + row for _ in range(height))
    payload = b"\x89PNG\r\n\x1a\n"
    payload += _png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))
    payload += _png_chunk(b"IDAT", zlib.compress(raw))
    payload += _png_chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)


def self_test() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        reference = root / "references/locked/v1/01-hero.png"
        _write_png(reference, 8, 6, (10, 20, 30))
        dimensions = {"desktop": (8, 6), "ultrawide": (10, 7), "mobile": (4, 8)}
        captures: dict[str, str] = {}
        for index, (name, size) in enumerate(dimensions.items(), start=1):
            capture = root / f"qa/{name}/01-hero.png"
            _write_png(capture, size[0], size[1], (40 * index, 50, 60))
            captures[name] = str(capture.relative_to(root))
        (root / "docs").mkdir(parents=True)
        (root / "docs/restoration-plan.md").write_text("# hero contract\n", encoding="utf-8")
        marker = "<!-- identity-section:hero status=pass -->\n"
        (root / "docs/fidelity-ledger.md").write_text(marker, encoding="utf-8")
        (root / "docs/fresh-review.md").write_text(marker, encoding="utf-8")
        manifest = {
            "schema_version": 1,
            "reference_lock_version": "v1",
            "source_strategy_locked": True,
            "review_scope": "all_sections",
            "viewports": {name: {"width": size[0], "height": size[1]} for name, size in dimensions.items()},
            "fidelity_ledger": "docs/fidelity-ledger.md",
            "fresh_review": "docs/fresh-review.md",
            "fresh_review_mode": "fresh-thread",
            "final_status": "pass",
            "sections": [
                {
                    "id": "hero",
                    "reference": {
                        "path": str(reference.relative_to(root)),
                        "sha256": sha256(reference),
                    },
                    "render_contract": "docs/restoration-plan.md",
                    "topology": {"kind": "section-specific", "shared_with": [], "reason": "unique hero grid"},
                    "captures": captures,
                    "gates": {gate: "pass" for gate in GATES},
                    "status": "pass",
                }
            ],
        }
        manifest_path = root / "docs/identity-evidence.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        assert validate(root) == [], validate(root)

        _write_png(reference, 8, 6, (99, 20, 30))
        assert any("SHA-256 mismatch" in error for error in validate(root))
        _write_png(reference, 8, 6, (10, 20, 30))

        manifest["reference_lock_version"] = "v2"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        assert any("lock version" in error for error in validate(root))
        manifest["reference_lock_version"] = "v1"

        (root / "docs/fidelity-ledger.md").write_text("heroic workflow: pass\n", encoding="utf-8")
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        assert any("pass marker" in error for error in validate(root))
        (root / "docs/fidelity-ledger.md").write_text(marker, encoding="utf-8")

        manifest["sections"][0]["topology"] = {
            "kind": "shared",
            "shared_with": ["ghost"],
            "reason": "same grid",
            "shared_geometry": "same columns",
            "responsive_behavior": "same stack",
        }
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        assert any("unknown section" in error for error in validate(root))
        manifest["sections"][0]["topology"] = {
            "kind": "section-specific",
            "shared_with": [],
            "reason": "unique hero grid",
        }

        desktop_capture = root / captures["desktop"]
        desktop_capture.write_bytes(reference.read_bytes())
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        assert any("copy of the locked reference" in error for error in validate(root))
        _write_png(desktop_capture, 8, 6, (40, 50, 60))

        manifest["sections"][0]["status"] = "fix"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        assert any("status" in error for error in validate(root))
        manifest["sections"][0]["status"] = "pass"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        (root / captures["mobile"]).unlink()
        assert any("missing capture" in error for error in validate(root))
    print("verify_identity_run self-test passed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?", help="identity website project root")
    parser.add_argument("--manifest", default="docs/identity-evidence.json")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if not args.project_root:
        parser.error("project_root is required unless --self-test is used")
    errors = validate(Path(args.project_root), args.manifest)
    if errors:
        print("identity evidence validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("identity evidence validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
