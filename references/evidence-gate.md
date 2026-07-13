# Identity 运行证据门槛（Evidence Gate）

精致、专业、参考图驱动的个人网站必须执行本协议。它把参考图锁定和最终视觉 QA 变成可检查的落盘证据，不能只靠 agent 在进度消息里自述完成。

## 1. 不可跳过的产物

实现前必须创建：

- `references/locked/<version>/`：不可覆盖的已确认 section 参考图；不得修改锁定版本中的文件
- `docs/restoration-plan.md`：逐 section render contract、来源策略、几何、拓扑归属、响应式行为和素材 manifest
- `docs/identity-evidence.json`：可机器检查的参考图哈希、截图路径、硬门槛结果和最终状态

最终交付前必须创建：

- 每个 section 在 `desktop`、`ultrawide` 和 `mobile` 下各一张 PNG 截图
- `docs/fidelity-ledger.md`：逐 section 的参考图与渲染结果差异、判断和修正
- `docs/fresh-review.md`：fresh-context 审查，必须覆盖每一组 section 对照，不能只抽查部分

缺少证据时，状态只能是 `not verified`，绝不能写成 `pass`。

## 2. 参考图确认前锁定来源策略

对每个可识别的人物、公司、产品、作品、出版物或项目，在第二步确认前决定主要证据属于哪一类：

- 用户提供或官方素材
- 不承载事实主张的生成氛围或辅助场景
- 用户明确批准的 `replace-later` 替身
- 代码原生证据

锁定参考图前，先把可用的官方素材或用户素材纳入构图。不要先确认一张更强的生成占位构图，再计划在锁定后换成明显不同的官方素材。

如果后续来源改变主体、出处、媒介、轮廓、宽高比、裁切、视觉重量、焦点层级或响应式行为，创建新的参考图版本并重新执行第二步。不得覆盖锁定参考图，也不得以 `intentional deviation` 为由继续使用旧基线。

## 3. 版本化参考图锁定

把已确认参考图保存到新目录，例如：

```text
references/locked/v1/01-hero.png
references/locked/v1/02-work.png
```

在 `docs/identity-evidence.json` 中记录每张参考图的 SHA-256。重新生成时创建 `v2`、`v3` 或其他明确版本。保留旧版本，让后续审查可以发现质量回退或基线漂移。

只有在受影响的完整参考图组重新通过审查后，才能切换 active version。用户要求跳过确认暂停，不代表可以静默替换参考图。

## 4. Section 拓扑归属

写代码前，为每个 section 记录一种拓扑决策：

- `section-specific`：该 section 的网格、坐标系、flow 或构图不能与其他 section 共用结构组件
- `shared`：只有当已确认参考图具有相同几何和响应式行为时，才允许复用一个命名结构

可以共享字体 token、颜色、按钮、rail 和小型 primitive。除非证据 manifest 明确写出共享 section、共享几何、响应式行为和理由，否则禁止共享结构定位。

不要让通用组件抹掉 section 专属布局。当参考图有独特的三栏网格、流程行、竖排文字、媒体框或 exclusion zone 时，直接实现该拓扑，或建立明确 variant。

## 5. 按 Section 切片实现和验证

每个 section 依次执行：

1. 根据 render contract 实现该 section
2. 在已确认的桌面参考图 viewport 下截图
3. 使用 `view_image` 同时查看参考图和最新截图
4. 修复所有可见偏差后，再继续下一个 section
5. 补齐 ultrawide 和 mobile 截图，并完成全部硬门槛

只查看了部分 section 时，不得宣称多个 section 已通过。技术检查、素材齐全、console 无错误或哈希稳定，都不能证明视觉保真。

## 6. 证据 Manifest

按以下结构写入 `docs/identity-evidence.json`：

```json
{
  "schema_version": 1,
  "reference_lock_version": "v1",
  "source_strategy_locked": true,
  "review_scope": "all_sections",
  "viewports": {
    "desktop": { "width": 1672, "height": 941 },
    "ultrawide": { "width": 2200, "height": 1200 },
    "mobile": { "width": 390, "height": 844 }
  },
  "fidelity_ledger": "docs/fidelity-ledger.md",
  "fresh_review": "docs/fresh-review.md",
  "fresh_review_mode": "fresh-thread",
  "final_status": "pass",
  "sections": [
    {
      "id": "hero",
      "reference": {
        "path": "references/locked/v1/01-hero.png",
        "sha256": "<sha256>"
      },
      "render_contract": "docs/restoration-plan.md",
      "topology": {
        "kind": "section-specific",
        "shared_with": [],
        "reason": "portrait、route 和 evidence map 使用独立坐标系"
      },
      "captures": {
        "desktop": "qa/desktop/01-hero.png",
        "ultrawide": "qa/ultrawide/01-hero.png",
        "mobile": "qa/mobile/01-hero.png"
      },
      "gates": {
        "visual_meaning": "pass",
        "hierarchy": "pass",
        "personal_evidence": "pass",
        "composition": "pass",
        "typography": "pass",
        "asset_crop": "pass",
        "overlap": "pass",
        "responsive": "pass",
        "reference_fidelity": "pass"
      },
      "status": "pass"
    }
  ]
}
```

当环境支持独立审查者时，使用 `fresh-thread` 或 `independent`。只有确实无法获得独立审查者时才能使用 `self-blind`，并且该审查只能接收 brief 加原始参考图/渲染图对照。

`docs/fidelity-ledger.md` 与 `docs/fresh-review.md` 必须为每个 section 写入精确标记：

```text
<!-- identity-section:hero status=pass -->
```

`hero` 必须与 manifest 中的 section `id` 完全一致。不能用普通子串、近似名称或只在解释性文字中提到 section 来代替标记。

## 7. 确定性完成检查

最终交付前运行：

```bash
python3 <identity-skill>/scripts/verify_identity_run.py <project-root>
```

验证器检查：

- 参考图位于 manifest 声明的锁定版本目录，并且哈希未变化
- 所有 contract、ledger、review 和截图都存在
- 截图是 PNG，尺寸与声明的 viewport 一致
- 每个 section 的全部硬门槛和最终状态都是 `pass`
- 每个 section 都在两份书面审查中有精确的 `status=pass` 标记
- shared topology 引用的 section 确实存在
- 渲染截图不是换名复制的锁定参考图

退出码 `0` 只证明证据完整，不证明视觉质量。最终完成必须同时满足验证器通过和真实的逐图对照审查通过。

## 8. 自动继续

当用户要求自动接受推荐方案或不做中间确认时：

- 只跳过等待暂停
- 不跳过审查、产物、重新生成或证据门槛
- 把 auto-continue 理解为“门槛通过后继续”，不能理解为“自动标记通过”
- 验证器失败或 fresh reviewer 返回 `fix` / `redesign-required` 时继续修正

缺少所需证据时，不得宣布完成、把 goal 标记为完成，或称构建已经通过保真验证。
