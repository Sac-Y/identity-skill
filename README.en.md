<sub>🌐 <a href="README.md">中文</a> · <b>English</b></sub>

<div align="center">

# Identity Skill

> *"Hand it the reference images. Get back a personal site that actually matches them."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Codex](https://img.shields.io/badge/Codex-Ready-black)](https://openai.com/codex)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-blueviolet)](https://skills.sh)

<br>

**Reference images first, code second. You review the design before a single line is written.**

Use Image 2 to turn each section into a reference image for you to approve, then rebuild it 1:1. The design step goes to the strongest image model — covering Codex's weak spot — so the design is seen and locked before any code exists.

```
npx skills add Sac-Y/identity-skill
```

Built mainly for **Codex** — installed, it triggers from a plain sentence.

[Demo](#demo) · [Why](#why) · [How it works](#the-five-step-workflow) · [Install](#install--use)

</div>

---

## Demo

All the sites below were generated with this skill:

**1 · Elon Musk**

https://github.com/user-attachments/assets/8396b561-5f30-40a8-92d0-e8655337193c

**2 · links (well-known China-based travel & photography blogger)**

https://github.com/user-attachments/assets/54c89d13-f7a7-4e0c-ba77-5f9b236b2cda

**3 · Sac (repo author)**

https://github.com/user-attachments/assets/31ccce26-ace5-41e4-909d-12603cce96b6

---

## Why

Ask an agent to build a site and it usually starts coding right away — you can't see the design until it's done, and its taste is unreliable.

This skill flips that: it first turns the design into reference images for you to approve, then rebuilds them faithfully. You lock the design before any code; implementation only has to reproduce it.

---

## The Five-Step Workflow

Every step has a concrete output, and the first four are separated by **blocking confirmation gates** — you decide at the key points instead of waiting for a whole wrong site.

| Step | What it does | Output | Gate |
|------|--------------|--------|------|
| **1 · Content & style lock** | Reads your resume / LinkedIn / project links, decides the site shape and sections, proposes up to 3 **visually concrete** style directions | Content & site-shape doc + style options | ✅ Confirm content & style |
| **2 · Reference-image lock** | One horizontal reference image per section, plus a consistency + monotony audit (incl. the "grey-block test") | Section reference set | ✅ Accept references |
| **3 · Asset split list** | Decomposes each reference: what stays code, what needs a background image, what needs a foreground asset — and **measures each asset's geometry** (bounding box, aspect ratio, width %) | Reference→build map + asset manifest | ✅ Confirm the split |
| **4 · Asset generation review** | Generates only approved assets, each **anchored to its reference region**, then inspects them one by one | Finished assets + restoration brief | ✅ Accept assets |
| **5 · Faithful rebuild & QA** | Hands off to the builder contract for a 1:1 build, compares each section to its reference, and **reconciles geometry with DOM numbers** | Website + fidelity ledger | — |

---

## Install & Use

```bash
npx skills add Sac-Y/identity-skill
```

Once installed, just describe what you want inside Codex:

```
"Use personal-website to build me a job-hunting personal site, I have a LinkedIn"
"Rebuild these reference images into a webpage, 1:1"
"Make me a portfolio site, be bold with the style, give me a few directions to pick from"
```

It starts from step one and pauses at each confirmation gate for your call.

### Dependencies & Compatibility

- **Image generation**: prefers the installed `imagegen-frontend-web`; otherwise reads the bundled adaptation, or writes prompts for you to paste into GPT web Image 2.
- **Frontend build**: prefers the installed Build Web Apps `frontend-app-builder`; otherwise uses the bundled Chinese translation.
- **Asset splitting**: bundled `reference-asset-splitter`, no separate install.
- All three companion references ship with the skill — **installing this one is enough**.

---

## Roadmap

Still iterating. Coming up:

- **Beyond Codex**: usage examples for other agents, and image generation via APIs beyond Image 2.
- **Motion**: give generated sites the interactions and animation you want.
- **More styles**: refine the design taste, add preset templates in a range of styles.
- **Flow polish**: keep refining the overall design flow.

Watch this repo — updates are ongoing.

---

## Acknowledgments

Step 2's reference-image generation uses [Taste Skill](https://github.com/Leonxlnx/taste-skill)'s `imagegen-frontend-web` (by [Leonxlnx](https://github.com/Leonxlnx) · MIT). Thank you!

---

## License

[MIT](LICENSE) © Sac-Y
