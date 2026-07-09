<sub>🌐 <b>中文</b> · <a href="README.en.md">English</a></sub>

<div align="center">

# Site Builder Skill

> *「给它参考图，拿回一个 1:1 还原的个人网站。」*
> *"Hand it the reference images. Get back a personal site that actually matches them."*

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Codex](https://img.shields.io/badge/Codex-Ready-black)](https://openai.com/codex)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-blueviolet)](https://skills.sh)

<br>

**先出参考图，再写代码。设计你先过目，实现照图还原。**

用 Image 2 把每个分区的设计出成参考图，你确认后再做 1:1 还原。设计这一步交给最强的图片模型，补上 Codex 的短板；写第一行代码前，你已经看过并锁定了设计。

```
npx skills add Sac-Y/site-builder-skill
```

主要面向 **Codex**，装好后直接说话即可触发。

[为什么需要它](#为什么需要它) · [怎么工作](#五步工作流) · [安装与使用](#安装与使用)

</div>

---

## 为什么需要它

让 agent 做网站，通常是它直接开始写代码——你看不到设计长什么样，只能等它做完，而它的审美又不稳定。

这个 skill 反过来：先用 Image 2 把每个分区的设计出成参考图给你确认，再照图高保真还原。你在写代码前就锁定了设计，实现只负责还原。

---

## 五步工作流

每一步都有明确产物，前四步之间有**阻塞式确认关卡**——你在关键决策点拍板，而不是等它做完一整个错的网站。

| 步骤 | 做什么 | 产物 | 确认关卡 |
|------|--------|------|----------|
| **1 · 内容与风格锁定** | 读你的简历/LinkedIn/项目链接，定站点形态和分区，推荐最多 3 个**可视觉想象**的风格方向 | 内容与站点形态文档 + 风格选项 | ✅ 确认内容和风格 |
| **2 · 参考图锁定** | 每个分区出一张横向参考图，做一致性 + 单调性双向审查（含「灰块测试」） | 分区参考图集合 | ✅ 接受参考图 |
| **3 · 素材拆分清单** | 逐张拆解参考图：哪些留代码、哪些出背景图、哪些出前景素材，并**测量每个素材的几何**（包围盒、长宽比、占宽 %） | 参考图→构建映射 + 素材清单 | ✅ 确认拆分方案 |
| **4 · 素材生成评审** | 只生成已批准的素材，每张**锚定参考图区域**生成、生成后逐一对照检查 | 素材成品 + 复刻简报 | ✅ 接受素材 |
| **5 · 高保真复刻与 QA** | 交给 builder 契约做 1:1 实现，逐区对照参考图，**用 DOM 数字对账几何** | 网站 + 保真台账 | — |

---

## 安装与使用

```bash
npx skills add Sac-Y/site-builder-skill
```

装好后，在 Codex 里直接描述你的需求即可触发：

```
「用 personal-website 帮我做个求职用的个人网站，我有 LinkedIn」
「照着这几张参考图 1:1 还原成网页」
「帮我做个作品集站，风格大胆一点，给我几个方向选」
```

它会从第一步开始，在每个确认关卡停下来等你拍板。

### 依赖与兼容

- **图像生成**：优先用已安装的 `imagegen-frontend-web`；没有则读内置适配版，或写好提示词让你贴到 GPT web Image 2。
- **前端实现**：优先用已安装的 Build Web Apps `frontend-app-builder`；没有则用内置中文翻译版。
- **素材拆分**：内置 `reference-asset-splitter`，无需单独安装。
- 三份配套引用都已随本 skill 打包，**装这一个就够了**。

---

## 敬请期待

还在持续迭代，接下来计划：

- **不止 Codex**：补上其他 Agent 的使用示例，图片生成也接入 Image 2 之外的模型 API。
- **动效**：让生成的网站带上你想要的交互与动效。
- **更多风格**：改进设计 taste，增添多种不同风格的预设模板。
- **打磨流程**：继续完善整体的设计流程。

关注本仓库，持续更新中。

---

## 致谢

第二步参考图生成使用了 [Taste Skill](https://github.com/Leonxlnx/taste-skill) 的 `imagegen-frontend-web`（by [Leonxlnx](https://github.com/Leonxlnx) · MIT）。感谢！

---

## License

[MIT](LICENSE) © Sac-Y
