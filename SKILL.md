---
name: identity-skill
description: "通过分阶段参考图驱动流程创建有辨识度的个人网站：内容与风格锁定、参考图锁定、素材拆分确认、素材生成审核，然后高保真复刻与 QA。适用于用 Codex、Image 2、参考图、生成素材或高质量 image-to-code 流程制作、重设计或复刻个人网站、作品集、创作者网站、创始人网站或个人 IP 网站。"
---

# 个人网站（Personal Website）

## 核心规则

不要直接进入代码。把网站视为一个分阶段参考图驱动项目：

1. 内容与风格锁定
2. 参考图锁定
3. 素材拆分清单
4. 素材生成审核
5. 高保真复刻与 QA

用户可见流程默认有四个阻塞式确认：

1. 确认完整的内容与风格 brief，包括站点形态、section 规划、内容充分性、以及已选择或用户提供的视觉方向
2. 在一致性、节奏和可实施性审查之后，确认参考图组
3. 生成或查找新素材前，确认素材拆分清单
4. 页面代码实现前，确认已生成/已整理素材和复刻执行 brief

参考图组确认后，不要直接进入实现。先检查每张已确认参考图，产出给用户看的素材拆分清单，并等待确认。清单确认后，只生成、查找或整理清单里批准的素材。素材完成后，列出最终路径、检查结果和简短复刻执行 brief；等待用户接受、要求重生成，或修改拆分。只有这一步确认后，才能开始高保真复刻。

旧的 lightweight pre-build design note 合并进素材审核输出，变成一份简短的复刻执行 brief。它不是额外独立确认点：用户在代码前同时确认素材结果和复刻执行 brief。

不要把后续阶段压缩成普通前端构建。已确认参考图不是 moodboard。写代码前，每张参考图都必须有已确认的 render contract，并拆成代码负责区域、融合场景、独立媒体、身份/真实来源素材、视觉锚点，以及最终来源和状态决策。

硬停止条件：在素材拆分清单已确认、批准素材已生成或整理、素材审核与复刻执行 brief 已接受之前，不要创建或修改 HTML、CSS、JS、React、route 或 component 文件。只在进度提示里说“我会拆参考图”不算完成。

精致参考图驱动项目还要执行证据硬停止条件：读取 `references/evidence-gate.md`。缺少要求的落盘证据时，状态只能是 `not verified`，不能写 `pass`。用户要求跳过确认暂停，只代表门槛通过后自动继续；不代表自动通过、静默替换参考图、跳过审查或无证据完成。

如果用户只有部分资料，先审查缺口，并优先建议更省力的资料输入方式，而不是马上要求用户手写所有内容。如果用户已经有确认过的内容、参考图和素材，可以直接跳到相关审查、素材审核或复刻阶段，但代码前仍要保留相同确认边界。

## 执行纪律

在阶段之间推进时，说明当前假设、下一个可验证目标，以及完成它的检查方式。如果请求有多种解释，先把选项说清楚并询问，再进入具体方向。

保持修改克制：

- 不要添加用户没有要求或确认的 section、交互、内容、route、素材类型或配置
- 编辑现有项目时，只改已确认范围内必要的文件，并匹配项目现有风格
- 只移除本工作流新增后变成无用的代码、素材或 import；无关的既有死代码只提及，不删除
- 优先使用能让下一阶段可靠推进的最小设计说明、素材清单、prompt 组或实现改动
- 多步骤工作要有足够具体的成功标准，避免靠猜测推进
- 每次只实现并验收一个 section slice；只检查了部分 section 时，不得宣称多个 section 已通过

## 语言与本地化表达

用户可见引导要匹配用户主要语言。用户用中文提问时，进度提示、阶段衔接、确认请求和选项标签都使用中文，例如 `第一步 / 内容与风格锁定`、`接下来进入第二步`。用户用英文提问时，使用英文，例如 `Step One / Content and style lock`、`Next I will move to Step Two`。如果对话中英混合，优先遵循用户最新的明确偏好，或最近一条实质请求的语言。

面向用户的提示、阶段转场、确认请求和选项标签默认使用中文；必要的文件名、命令、字段名和技术术语保留英文，以免改变执行契约。

阶段名也要完整翻译。中文用户应写 `第五步 / 高保真复刻与 QA`，不要写 `Step Five / Build and QA` 这类中英混合标签。

## 内置 Companion Skills

本 skill 内置 companion reference，因此工作流不依赖用户额外安装其他 skill：

- `references/imagegen-frontend-web.md`：用于第二步个人网站参考图生成硬契约
- `references/visual-quality-gate.md`：用于第二步和第五步的真实意义、层级、留白、裁切、重叠、作者性与 fresh-context 审查
- `references/evidence-gate.md` 与 `scripts/verify_identity_run.py`：用于不可覆盖参考哈希、逐 section 截图证据、拓扑归属和确定性完成校验
- `references/reference-asset-splitter.md` 与 `references/split-patterns.md`：用于第三步三轴素材裁决和真实纠错案例
- `references/frontend-app-builder.md`：用于素材审核后的高保真实现和 QA

个人网站参考图生成阶段，无论是否安装独立 `imagegen-frontend-web`，都必须读取 `references/imagegen-frontend-web.md`。目标是精致、专业、有辨识度或 Awwwards 级时，第二步和第五步还必须读取 `references/visual-quality-gate.md`。这些内置文件是本工作流的硬契约；独立 skill 可以补充更广的创意词汇，但不能覆盖已确认 brief、style fingerprint、meaning contract、视觉质量门槛、素材预算和可实施性规则。

素材裁决阶段，若已安装 `reference-asset-splitter` 就使用安装版，否则使用内置版本；两边必须保持同一套 classifier 和案例。用户已确认 brief 与本 skill 的硬阶段边界优先级高于 companion 默认规则。第五步仍优先使用安装版 `frontend-app-builder`，内置副本作为 fallback。

如果 companion skill 没有安装，不要卡住，不要假装 `@skill` 调用可用，也不要为了继续流程就要求用户安装。读取本包内置 companion reference，并把它作为本地最低执行契约。

只有当用户明确想要可独立安装的组件时，才讨论单独安装 companion skill。正常路径里，安装 `identity-skill` 一个 skill 就应该足够。

如果没有任何图片生成工具，写可复制的 prompt，让用户粘贴到 GPT web Image 2 或其他图片工具，或请用户提供自己的参考图。如果用户完全跳过参考图，则把构建视为较低 fidelity，并明确说明视觉 QA 只能对照文字 brief，不能对照已接受参考图。

## 阶段提示协议

每个用户可见阶段结尾都要给出清晰进度提示：

- 当前进度：`第一步 / 阶段名称`
- 已完成：刚产出的具体结果
- 仍缺失或存在风险：只列真正影响推进的阻塞点
- 用户现在可以做什么：确认、修改某个命名部分、提供缺失资料、或选择选项
- 下一步：说明下一阶段名称以及会发生什么

不要让用户停在一个隐含的断点。如果流程会在没有阻塞确认的情况下继续，明确说明会继续以及原因。

## 第一步：内容与风格锁定

先判断适用哪条内容路线。不要让用户手动重复输入那些可以从已提供文件、链接、简历、profile、笔记、写作样本、项目文档、截图或现有网站中读取的信息。

### 资料输入路线

使用以下路线之一：

- 资料充足路线：用户提供了简历、CV、LinkedIn、个人主页、作品集、项目链接、Notion/Markdown 文档、个人简介、媒体包、社交主页、写作归档或类似材料。读取可访问内容，提取已确认事实、可用于 section 的内容单元、链接、素材和缺口。只问会影响网站的定向补充问题。
- 简略 brief 路线：用户给了目标或身份，但支持材料很少。先邀请用户提供更省力的输入，例如简历、现有介绍、项目链接、写作链接、照片、参考网站或截图。如果用户不想提供文件，再使用下面的引导问题。
- 从零开始路线：用户没有材料，或希望从零梳理。把引导问题一次性集中提出，不要一题一题长访谈。
- 快速 demo 路线：用户明确强调速度或粗糙原型。可以使用轻量 mock 内容，但所有编造的事实、项目、引用、指标、链接或个人简介细节都必须标记为占位内容，正式版本前需要替换。

引导问题路线应紧凑收集：

- 目标：简历、求职、作品集、创作者/个人 IP、顾问、创始人/高管介绍、演讲/媒体页，或其他目的
- 受众：谁会访问，看完后希望他们做什么
- 定位：身份标签、能被记住的一句话、语气边界
- 证明材料：经历、项目、写作、产品、客户、媒体报道、演讲、奖项或其他证据
- 项目细节：每个重要项目的背景问题、你的角色/行动、结果、链接/媒体，以及希望别人记住什么
- 素材和边界：头像、logo、截图、文档、链接、不可用或敏感内容，以及不能生成或不能夸大的内容
- 用户偏好：站点信息密度、是否倾向单页或多页、喜欢的参考、不喜欢的风格、后续维护意愿

### 内容与站点形态文档

对于精致个人网站、个人 IP 网站、作品集、Awwwards 级方向，或任何设计质量重要的场景，进入图片前先产出内容与站点形态文档。快速 demo 可以保留同样结构，但写得更短。

文档应包括：

- 资料覆盖：使用了哪些文件、链接、笔记或用户回答
- 已确认事实：只写用户提供或来源支持的事实
- 未确认草稿内容：清楚标记 agent 提议的文案、示例、占位、推断 claim 或缺失链接
- 站点目标与受众：这个网站要完成什么、给谁看
- 访客记忆点：访客应该记住的一到三件事
- 站点形态推荐：单页、一页简历、首页加 case study、多页作品集、创作者 hub、顾问 landing page，或其他形态
- 推荐理由：为什么这个形态适合用户目标、内容量、证明深度和维护意愿
- 可选替代方案：可行但不如主推荐的更轻或更完整结构
- section 规划：每个 section 的目的、必需内容、内容单元、链接/素材和状态（`ready`、`needs detail`、`placeholder` 或 `cut`）
- 内容充分性风险：空泛、模板化、虚假、拥挤、缺少支撑或不值得保留的 section

站点形态必须根据用户目标和资料密度推荐，不要默认套五六个 section。简历或求职用途通常只需要单页或一到两页。深度作品集可能需要 case-study route。创作者、创始人或顾问网站只有在内容支撑时，才需要更强叙事或转化路径。

用于参考图的所有内容都必须来自用户提供或用户明确批准。agent 可以提出内容来补缺口，但这些内容只是草稿，不是已确认事实。不要因为内容写得合理或好看，就把 agent 提议内容当作已确认。

第二步确认前，先锁定每个可识别人物、公司、产品、作品、出版物或项目的证据来源策略。尽早收集可用的用户素材或官方素材，让参考图直接围绕真实证据构图；不要先确认一个更强的生成占位构图，再计划在锁定后替换成视觉重量、比例或主体不同的官方素材。

### 风格推荐

内容和站点形态足够清楚后，基于内容、用户偏好、受众、网站目的和已有参考，推荐最多三种视觉方向。用户可以选择一种、混合多个选项，或提供自己的视觉方向/参考。

风格选项必须是视觉概念，而不只是定位标签。不要只给“国际学生精品简历”“金融科技产品研究员”“AI + Finance Portfolio”这类只区分受众或职业叙事的选项。这些标签可以解释为什么适合，但选项本身必须让用户在生成图片前就能想象页面长什么样。

每个风格选项应简要覆盖：

- 视觉概念名：用短标签描述画面气质，而不是只写个人角色
- 情绪和定位匹配
- 色彩方向：3-5 个具体颜色或颜色角色，必要时给 hex
- 字体气质：display/body 的字体性格和粗细对比
- 首屏构图：姓名、headline、头像/媒体、CTA、证明线索分别如何出现
- 布局密度与 section 节奏：单页克制、editorial 节奏、bento 证明块、case-study 深度，或其他具体节奏
- 图片或素材处理方式：头像裁切、项目截图、文档卡片、数据视觉、editorial 照片、抽象背景或代码渲染图形
- UI chrome 与导航感觉：header 密度、wordmark、CTA 形状、边框、圆角、icon 风格和 active state
- 动效性格
- 用户会看到什么：用一句话描述屏幕直观印象
- 为什么适合这个人和这种站点形态
- 主要风险或取舍

如果某个风格选项不能被描述成一个可见的网站画面，先重写再展示给用户。如果用户目标是职业定位，要把定位翻译成视觉决策，而不是让选项标题承担全部表达。

必要时使用这个紧凑的风格选项格式：

```text
选项 A — Editorial Resume / 墨色纸感
色彩：暖白 #F7F3EC、墨黑 #171717、灰蓝 #6B7280、强调蓝 #2563EB。
字体：克制 serif display + 干净 sans body；专业但不装饰化。
首屏：姓名和一句定位左对齐，置于大面积纸感留白中；右侧是安静裁切的头像或 LinkedIn 风格照片，下方放两个证明链接。
节奏：单页简历流，section 平静，项目证明用小型卡片承载。
直观感受：像一份精致的国际候选人 editorial CV，而不是创业公司 landing page。
风险：如果用户想要更强个人品牌，会显得辨识度偏弱。
```

在用户确认完整内容与风格 brief 之前，不要生成参考图。如果用户选择了风格选项且没有反对内容文档，只有在你的提示明确说明“这会同时锁定内容和风格”时，才把该回复视为第一次阻塞确认。

使用这个第一步收尾提示形态：

```text
当前进度：第一步 / 内容与风格锁定
我已经准备好：资料来源摘要、已确认事实、站点形态推荐、section 规划、内容风险和风格选项。
请确认或修改：
1. 站点形态和 section 规划
2. 所有标记为未确认的内容
3. 视觉方向：选择一个选项、混合多个选项、修改色彩/布局，或提供你自己的参考
确认后，我会进入第二步，生成或准备各 section 的参考图。
```

## 第二步：参考图锁定

使用 section 级参考图作为视觉事实来源。

参考图 prompt 必须基于已确认的内容与风格 brief：已批准内容、已批准站点形态、已选择或用户提供的视觉方向、全局 chrome 规则，以及每个 section 的具体内容单元。用户期待高质量个人网站时，不要基于薄 brief 或未批准的 agent 提议内容生成参考图。

本阶段始终读取 `references/imagegen-frontend-web.md`。如果独立 `imagegen-frontend-web` 可用，在内置个人网站硬契约下使用它补充更广的 art direction。参考图组必须做到每个已确认 section 一张横向图、强构图、统一个人 IP 世界，以及可以真正实现的图片拓扑。

如果用户偏好 GPT web Image 2，则为用户写可复制过去的 prompt，而不是直接生成图片。

### 参考图生成计划

生成任何 section 前，先准备一份简洁的参考图生成计划。它属于第二步内部 artifact，不增加新的用户确认门。已有项目目录时，把它写入还原文档或小型 `docs/reference-production-plan.md`；没有目录时，保留在第二步工作输出中。

先锁定整组共用的 style fingerprint：

- 精确色彩角色与 hex 值
- display/body/label/nav 字体角色和相对字号
- 全局 chrome 几何、边框/圆角/阴影语言和 CTA 家族
- 材质、光线、纹理、照片调色、插画/icon 语言
- 密度范围、间距节奏、画布比例，以及最多一个可选 signature motif
- 不允许漂移的常量，以及每个 section 允许变化的一到两个维度

然后给每个 section 指定一份 render contract：

- `C0 code-only`：字体、布局和简单几何，不需要 raster 素材
- `C1 integrated-scene`：代码 UI 叠加在一张融合场景上；场景可以 full-bleed，也可以是有边界的视觉岛
- `C2 independent-media`：代码外壳加一到三个有独立意义的照片、截图、封面或产品 mock
- `C3 scene-plus-identity`：一张融合场景，加一张真实来源或 replace-later 的头像、logo、官方产品图

每份 render contract 必须写清：代码负责内容、允许的全站 shared material、融合场景边界、独立媒体槽、身份/真实来源素材、禁止融合项、响应式行为、文字安全区、素材预算，以及拓扑归属（`section-specific` 或命名并说明理由的共享结构）。高质量目标还必须补齐 `references/visual-quality-gate.md` 的 meaning 字段：三秒信息、个人证据、作者性设计动作、焦点层级、阅读路径、留白地图、语义图形含义、重叠清单、封闭排除区和首屏有效载荷。`C0 code-only` 表示 0 个 section 专属 raster；如果纸面或扫描条属于已锁定 fingerprint，可以复用一到两个显式声明的全站材质。但它不代表一个内容不足、只靠大字撑满高度的 section 已经完成：除大字外还必须有第二个来自内容的设计决策，否则缩短、合并或重设计该 section。每种 shared material 只生成一次、全站只计一次。默认每个 section 一个主视觉焦点、最多一张融合场景、section 专属 raster 单元不超过三个；只有用户明确批准 dense evidence-wall 方向时才能超出。

先生成最能定义身份的 anchor section，通常是 Hero。后续 section 在同一批次生成；图片工具支持参考输入时，必须把 anchor 作为视觉指导，否则逐字复用同一份 style fingerprint。anchor 与后续图片之间不增加额外确认门。

默认输出：

- 每个 section 一张横向参考图
- 不要长竖版整页拼贴
- 不要细碎难读的多 section board
- 所有 section 保持一致的个人 IP 世界观
- 参考图应像真实网站截图，不像海报
- 代码负责的文字和控件要能与 raster 材质干净分离
- 静态融合场景保持为一个完整视觉单元；独立媒体槽之间不得出现跨边界阴影、反射或遮挡

把参考图组交给用户确认前，运行四重审查：

1. 视觉意义审查：执行 `references/visual-quality-gate.md` 的全部硬门槛，包括三秒传达、单一第一焦点、有目的的元素清单、个人特异性、完成的构图、密度上下限、有意义留白、图形语义、裁切完整性、重叠安全和响应式首屏有效载荷。一个 section 即使漂亮或可实现，只要想法、证据或构图薄弱，仍然失败。
2. 一致性审查：把每张图与精确 style fingerprint 对照，检查全局导航、字体角色、色板、间距、框体语言、图片调色、motif 和移动端逻辑。必须让人一眼看出属于同一网站。
3. 节奏审查：列出每个 section 的构图骨架并检查 variation envelope。可以有节制地变化 section 任务、尺度、对齐、裁切或密度，但不要强迫每屏成为全新视觉概念。运行 grey-block test：照片变成灰块后，至少一半 section 仍应通过字体、布局、色彩和结构保持设计感。
4. 可实施性审查：把每张图与 render contract 对照。如果代码文字与 raster 材质不可分离、独立素材共享硬阴影/遮挡、身份素材被融进生成场景、响应式重排需要在单张图内部搬动像素、未经批准超过素材预算，或出现计划外图片岛，该 section 失败。

参考图拓扑失败时使用 `redesign-required`：保持全站 style fingerprint，只重生成失败 section，再交给用户确认。不要把不可实施的参考图硬塞进第三步，用脆弱切片或低保真代码替代来补救。

审查通过的参考组确认后，把它复制进新的不可覆盖目录，例如 `references/locked/v1/`，并把每张图的 SHA-256 写进 `docs/identity-evidence.json`。不要覆盖已锁定文件；重生成或重构必须创建新版本并重新执行受影响的第二步审查。

当设计质量重要，或用户要求 taste guidance 时，同时读取 `references/taste-calibration.md` 和 `references/visual-quality-gate.md`。taste 样本负责校准可选视觉世界，质量门槛负责判断这个世界是否真正表达清楚并完成了设计。

使用这个第二步收尾提示形态：

```text
当前进度：第二步 / 参考图锁定
我已经准备好：全站 style fingerprint、每个 section 的 meaning 与 render contract、参考图，以及视觉意义/一致性/节奏/可实施性审查。
请确认或修改：
1. 接受这些图片作为构建目标
2. 指定要重新生成的 section
3. 在构建前调整视觉方向
图片确认后，我会进入第三步，正式产出素材拆分清单：哪些留在代码里、哪些是一张融合场景、哪些是独立媒体、哪些必须用真实来源、哪些需要 blocked、replace-later 或 redesign-required。我会等你确认后再生成或查找新素材。
```

## 第三步：素材拆分清单

参考图组确认后，先检查已接受参考图，不要生成素材，也不要写代码。本阶段产出给用户看的素材拆分清单，并停下来等待确认。

产出清单前，如果已安装 `reference-asset-splitter`，读取它和 `references/split-patterns.md`；否则读取内置 `references/reference-asset-splitter.md` 与 `references/split-patterns.md`。按顺序执行三轴 classifier：边界颗粒度、渲染介质、图片层级。不要把三件事压成一句“看起来很复杂”。

使用固定冲突优先级：真实身份/来源素材；live semantic 内容与无障碍；独立交互/替换/更新/响应式重排；code whitelist 与 raster signals；fusion 关系；素材预算；最后才是审美偏好。视觉复杂度本身既不能强制细拆，也不能证明代码可以高保真复刻。

目标是实用，不是过度规格化：告诉用户哪些可见部分应该留在代码里，哪些需要单独生成或收集素材，哪些需要透明/前景素材，哪些属于背景，哪些真实资产不能伪造，以及哪些判断一旦猜错会影响最后复刻效果。

本阶段创建或更新一个可见还原 artifact。可接受形式包括：

- `docs/restoration-plan.md`，合并参考图映射、素材 manifest 和后续复刻执行 brief
- `docs/reference-to-build-map.md` 加 `docs/asset-manifest.md`
- 如果仓库已有 docs 约定，也可以使用等价的项目内文档

artifact 必须在素材生成前、页面代码编辑前落地。它必须列出每张已确认参考图和每个 section/page。只在聊天里总结、隐藏推理或用一句进度提示说明，不满足要求。

给用户看的素材拆分清单应比内部 artifact 更短。每个 section 包括：

- 代码负责元素：文本、导航、按钮、布局、简单形状、标签，以及需要可编辑的动效
- 全站 shared material：可选的纸面、颗粒、扫描条或其他只生成一次并复用的 fingerprint 材质，或 none
- 融合场景素材：整段背景或有边界的融合场景、纹理、地图、照片场、桌面世界、卡片拼贴，或 none
- 独立媒体素材：头像、产品 mock、截图、照片、封面、单体插画，或 none
- 已有真实素材：用户提供照片、logo、产品截图、官方素材，或待复制的源文件
- 可生成素材：安全可生成的氛围图、装饰物、抽象产品 mock、背景或 stand-in
- blocked、replace-later 或 redesign-required：真实人物、官方品牌/logo/产品图、带 claim 的缺失截图，或无法忠实分层的参考图拓扑
- 为什么重要：如果素材边界判断错误，会造成什么复刻 fidelity 风险

### 素材边界规则

准备第三步素材拆分清单和第四步素材生成审核时，使用以下规则。

参考图存在后、写代码前，把三个判断轴分开执行：

1. 边界：只有独立交互、替换/更新、独立语义或响应式重排才强制细拆。移除代码节点和强制独立节点后，把存在叠压、跨物体阴影/反射、连续纹理、透视、光线或材质关系的静态 raster 物件合并。同一个 fusion group 默认一张素材，不看里面能数出几张卡片。
2. 介质：只有 live text、DOM 布局、纯色、普通边框/圆角/阴影、简单 CSS gradient、标准 icon、基础 grid/dot 和简单 SVG 几何可以 code-native。照片、不规则材质、手写/笔刷、复杂插画、密集 UI/product mock、自然纹理、3D、真实光影/反射或共享 raster 效果必须用图片。既需要 live 行为又需要 raster fidelity 时，用 hybrid：图片负责视觉，代码负责外壳、文字和交互。
3. 层级：`integrated-scene` 是与 section 绑定的一张融合视觉，可以 full-bleed，也可以只占 Hero 右侧；`independent-media` 是可独立替换的照片、截图、封面、mock、头像或单体插画。透明与否不决定分类。

默认每个 section 最多一张融合场景，raster 单元总数不超过三个。独立媒体槽各自成素材，融合静态群保持一张。所有最终文字、导航、按钮、表单、事实数据和交互留在代码里。允许整屏艺术背景，不允许把代码负责内容一起烘成整屏截图。

当 live text 无法从材质里分离、交互元素与另一层共享硬阴影/遮挡、真实身份素材不可逆地融入生成场景、移动端需要在单张图内部独立搬动像素，或重组依赖脆弱像素接缝时，使用 `redesign-required`，不要强拆。保持 style fingerprint，只把这个 section 退回第二步重生成。

每张已确认参考图都要在可见还原 artifact 中记录 reference-to-build map：

```text
Reference: 01-hero.png
Code layer: nav、headline、subhead、CTA group、portrait frame、proof labels
Integrated scene: hero-finance-desk.png，16:9，full-bleed，允许深色遮罩
Independent media: portrait.png，右侧 24% 宽；product-card-mock.png，下方中间 22% 宽
Must preserve: 深色桌面/金融照片氛围、左侧大标题比例、右侧头像卡、绿色 CTA、顶部导航间距
Allowed deviation: 生成图里的图表标签改为代码渲染的已确认文案
Risk trigger: 未确认的真实公司标记或用户头像需要先确认
```

每个 section 都必须覆盖所有有意义区域：semantic role、boundary triggers、code whitelist 结果、raster signals、fusion group、owner（`code` 或 `asset`）、placement（`integrated-scene`、`independent-media` 或 none）、reuse scope（`global` 或 `section`）、provenance、responsive mode、decision/status（`ready`、`generate`、`find/copy`、`code-native`、`replace-later`、`blocked` 或 `redesign-required`）、source/action 和 final path。若没有 section 专属图片，直接写清原因，并单列复用的 shared material。

记录素材 manifest（asset、role、boundary trigger、raster signal、fusion group、placement、reuse scope、provenance、reference box、aspect ratio、relative size、responsive mode、status、final path），这样复刻时可以把每个素材放进固定宽高比容器，而不是让图片原始尺寸驱动布局。

使用这个第三步收尾提示形态：

```text
当前进度：第三步 / 素材拆分清单
我已经准备好：reference-to-build map、素材决策清单和初版 asset manifest。
请确认或修改：
1. 哪些元素保持 code-native
2. 哪些融合场景和独立媒体要生成、复制或 replace-later
3. 哪些真实头像、logo、产品截图或官方素材不能生成
4. 清单里真正存在歧义的交互或替换假设
确认后，我会进入第四步，只生成或整理已批准的素材。我还不会编辑页面代码。有用时我可以并行处理已批准的素材组；如果你希望顺序执行，请直接说明。
```

## 第四步：素材生成审核

素材拆分清单确认后，只生成、复制、查找或整理已批准的素材。然后给用户展示素材结果和简短复刻执行 brief。用户接受素材审核前，不要开始页面代码实现。

素材审核应包括：

- 每个 ready 素材的最终路径
- 每个素材对应哪个 section 和哪个可见元素
- 来源：生成、用户提供、官方/复制、code-native，或 replace-later
- 检查结果：accepted、needs regeneration、weak but usable with named deviation、blocked，或 replace-later placeholder
- 复现素材所需的 prompt/source notes

每个图片素材只有两种合法来源：

1. 第一步 intake 中已经收集到的真实素材，例如用户照片、logo、产品截图或媒体文件。第四步不要临时要求用户补新素材，除非用户自己选择提供；到这一步仍未提供的内容，要生成 stand-in、使用 code-native placeholder、标记 `replace-later`，或在会造成误导时标记 `blocked`。
2. 新图片生成：必须锚定对应参考区域。写任何生成 prompt 之前，先重新打开已确认参考图，把目标区域**转录**成视觉清单：场景类型（纸质卡片拼贴 / 摄影场景 / 扁平插画 / UI mock / 纹理场）、每个主要物件及其大致位置、色板 hex 值、光线、材质、留白布局。生成 prompt 必须**从这份转录**写出——同场景类型、同物件清单、同构图同色板——绝不能从素材名或拆分清单的一行摘要写。如果出图工具支持输入图片，同时把参考区域作为视觉参照附上。只写内容类目（"创作者坐在桌前有笔记本和卡片"）而没有转录的 prompt 是缺陷：它等于授权模型自己发明一个不同的场景。素材内的占位文字要求写 "abstract unreadable placeholder bars and squiggles"——不要用 "greeked" 这个词，出图模型可能把它字面理解成希腊语文字。

已确认参考图是构建目标和 QA 基线，不是素材来源。不要把参考图区域 crop、screenshot、slice 或 extract 到构建里；裁切会继承低分辨率、烘焙文字和破边。manifest 里没有 `extract` 状态。参考区域像需要素材时，用视觉描述重新生成该元素，或替换为真实来源素材。

对应 section 构建开始前，先准备所有已批准素材。使用稳定名称保存到项目素材目录，不要直接使用原始生成 ID。每个素材生成后立刻与参考区域和第二步 render contract 并排六轴对照：场景类型、物件清单、构图与留白、色板与光线、与代码负责内容的干净分离、没有违反 forbidden-fusion 的跨边界阴影/遮挡/反射。场景类型不符、缺失两个以上主要物件、烘焙代码 UI，或违反禁止融合规则 = 自动重生成，绝不能当 ready 交付。其他缺陷要重生成或在素材审核里明确标记；不要用 CSS blend、filter 或 mask 掩盖缺陷。

融合场景应生成带既定文字安全区、且不含最终网站文案的 clean visual plate。独立媒体必须保持记录的宽高比和语义边界。如果素材无法满足已确认 render contract，把该 section 作为 `redesign-required` 退回第二步；不要在素材生成阶段偷偷发明新的拆分方法。

如果最终交付或真实来源素材相较已确认参考图改变了主角、来源、媒介类型、轮廓、宽高比、裁切、视觉重量、独立语义主体数量、焦点层级、主色块、响应式行为或个人 claim，把该 section 标记为 `reference-invalidated`。实现前必须退回第二步重新生成或重构参考图，不能用 `intentional deviation` 掩盖目标已经发生结构性变化。

任何已批准的必需素材仍处于 `generate` 或 `find/copy` 状态时，不要写页面代码。先把它解决为 `ready`，或有理由地改成 `code-native` 并对用户可见说明，或用已批准 placeholder 标记 `replace-later`，或因为 `blocked` 暂停。

有用且当前环境允许时，可以在第三步已批准范围内并行运行素材生成子 agent，按 section 或素材组拆分。子 agent 输出必须由父会话检查后才可信。

复刻执行 brief 替代旧的 lightweight pre-build design note。保持简短，附在素材审核里，不单独再开一个额外确认点。它应锁定：

- 当前 build owner 和来源：已安装的 `frontend-app-builder` skill 路径/名称，或 `references/frontend-app-builder.md` fallback
- 主要视觉基线和 section 顺序
- 全局 chrome：导航、logo/wordmark 处理、header 密度、active state、移动端行为
- 字体锁定：display、body、label 和 nav 角色必须保持一致
- 色板锁定：从已确认参考图取样精确 hex token（主色、次色、强调色、中性阶）；若交付素材的实际像素与之有偏差，以素材为准修正 token——素材烘死难改、代码便宜易调。实现层必须把这些定义为 design token 并只用 token，禁止逐 section 重新目测取色
- 必需动效或交互想法：只写影响体验的效果
- 最终素材路径和代码/素材边界
- 允许偏差：参考冲突、弱素材、移动端简化或有意调整
- QA 目标：每个渲染 section 要对照哪张参考图
- 风险触发项：任何需要在代码实现前暂停确认的内容

只有在保持已确认主体、几何、层级和意义时，偏差才属于低风险允许项。`reference-invalidated` 变化是风险触发项，不是 allowed deviation。

使用这个第四步收尾提示形态：

```text
当前进度：第四步 / 素材生成审核
我已经准备好：已生成/已整理素材、最终素材路径、检查备注和复刻执行 brief。
请确认或修改：
1. 接受素材和复刻执行 brief，进入复刻
2. 重生成或替换指定素材
3. 在实现前修改任意代码/素材边界
确认后，我会进入第五步，用选定 builder 契约开始高保真复刻。
```

## 第五步：高保真复刻与 QA

只有用户接受第四步素材审核和复刻执行 brief 后，才能开始实现。

进入第五步时，先读取 `references/evidence-gate.md`，再选择并说明当前 build owner，然后开始实现：

- 推荐路径：如果已安装 Build Web Apps 的 `frontend-app-builder` skill，读取它，并按它的 `Before Coding`、`Implementation`、`Verification` 和 `Final Response` 流程做结构化 image-to-code 还原；本 skill 提供内容/风格 brief、已确认参考图、已确认素材 manifest、复刻执行 brief 和风险确认点
- fallback 路径：如果没有安装 builder，读取 `references/frontend-app-builder.md`，并按内置还原契约执行

不要让第五步变成普通手写页面。builder 路径必须体现在复刻执行 brief 和最终 fidelity ledger 里。

每张已确认参考图都必须有 reference-to-build map，并且每个必需视觉素材都已 ready、明确 code-native，或用已批准 placeholder 标记 replace-later，才能开始实现。不要只是把参考图复制进项目目录，作为“第二步做过了”的证明；参考图要么作为对照目标使用，要么被拆成真实构建输入。

### 高保真复刻

只有在参考图已接受、还原 artifact 已存在、所有必需素材 ready 或明确批准为 code-native/replace-later，且用户接受第四步素材审核和复刻执行 brief 后，才开始实现。

构建由 builder 契约管理，不由本 skill 临时自由发挥。第五步入口要完整读取已安装的 Build Web Apps `frontend-app-builder` SKILL.md；如果没有安装，则读取 `references/frontend-app-builder.md`，并严格执行其 Before Coding、Implementation 和 Verification 流程。已接受参考图是它的 accepted concept；本 skill 的还原 artifact、素材 manifest 和复刻执行 brief 是它的设计系统提取和实现 inventory 输入。两者重叠时，采用更严格规则。

首次实现编辑前，必须确认以下全部成立：

- builder 契约已在本会话读取
- 还原 artifact 已存在，并包含每张已确认参考图的 reference-to-build map
- 素材 manifest 已存在，或已包含在同一个 artifact 里
- 每个必需素材状态都是 `ready`、`code-native` 或已批准 `replace-later`
- 已命名实现目标文件和写入范围

实现时：

- 保留 section 顺序、布局、间距节奏、色彩逻辑、字体气质和图片位置
- 将每个前景素材放入 manifest 记录的宽高比和相对尺寸容器中，并使用 object-fit；不要让图片原始尺寸决定布局
- display 字体尺寸要根据参考图测量（headline 高度相对 section 宽度），不要凭感觉；验证长文本不会被裁切
- 保持已接受参考图作为每个 section 的目标；不要凭记忆或文字 mood 实现
- 每个主要代码块都要映射回已批准的 section 视觉锚点，再进入下一个 section
- 文本、按钮、导航、交互和动效用代码实现
- 只有生成素材能带来真实视觉价值时才使用
- 避免把有辨识度的参考图实现成通用模板 section
- 如果某个 section 第一版渲染明显偏离参考图，停止并按视觉锚点重建该 section，不要只做表面修补

### Sub-Agent 分派

多 section 或多页面构建时，只在相关确认门通过后并行边界明确的工作：第二步后可并行参考图分析，第三步后可并行素材生成，第四步后可并行实现。子 agent 用来做边界明确的工作，不用来发明多套并行设计系统。

适合拆分为：

- 参考图分析 agent：每个 agent 负责一个页面或一组 section，产出 reference-to-build map 和素材需求
- 素材生成 agent：每个 agent 负责一组融合场景或独立媒体素材，产出稳定文件名和 prompt/来源说明
- 页面或 section 复刻 agent：只处理不重叠写入范围，并使用共享设计 token 和该范围的已确认参考图
- lead integrator：负责全局 chrome、共享 token、最终组装、浏览器 QA 和最终 fidelity ledger

使用当前环境可用的原生子 agent 工具。只并行已经处于批准阶段和范围内的工作；除非平台本身要求，不要仅为了 delegation 再增加一个阻塞确认点。阶段衔接时说明并行拆分，并尊重用户要求顺序执行的选择。

给子 agent 的消息只包含完成任务所需的最少上下文，但必须自洽：要读的 skill/reference、style fingerprint、render contract、参考图路径、准确输出文件名、目标宽高比、色板 hex、forbidden-fusion 规则和返回契约。收集结果后，父会话必须用 `view_image` 检查每个输出，确认后才可使用。

### 视觉 QA

QA 按 builder 契约的 Verification 流程加完整 `references/visual-quality-gate.md` 逐 section 执行：把每张已接受参考图和对应渲染 section 放在一起检查，不只看 overview；可行时按参考图原始尺寸截图；还要检查连续滚动转场、普通桌面、超宽屏和移动端；写 fidelity ledger；并把 placeholder box、用代码画出的概念素材替代物等 builder hard stop 视为失败。下面检查项是 identity-skill 的补充，不替代 builder 契约。

需要本地预览 URL 时，优先使用 `portless` 和项目专属 hostname，例如 `personal-site.localhost`，合适时添加小型复用脚本或 `portless.json`。只有 portless 不可用或用户要求 raw port 时，才使用 `localhost:<port>`。

检查：

- 布局比例和 section 节奏
- 字体尺寸、换行和间距
- 没有被裁切或溢出的文本，没有参考图中不存在的元素重叠
- 色彩和对比度
- 每个 section 仍满足第二步 render contract：没有计划外 raster 岛、没有缺失融合场景、没有把代码文字藏进图片，也没有违反 forbidden-fusion
- 素材位置、宽高比和裁切是否符合 asset manifest
- 三秒信息、个人证据、作者性设计动作和单一第一焦点在没有实现说明时仍然成立
- 每块大留白在真实渲染尺寸下仍承担 whitespace map 记录的功能；固定高度容器内容不足视为失败
- 每个 diagram、orbit、node、line、arrow 或 chart 都表达 semantic-graphic contract 记录的真实关系
- desktop、ultrawide、mobile 下的主体安全裁切、封闭排除区、首屏有效载荷、carousel 初始状态和独立语义媒体重叠都通过
- 没有素材或内容替换导致已确认参考图失效
- 按钮、导航、hover 和动效行为
- 移动端和桌面端一致性

交付前写简短的逐 section fidelity ledger：section、参考图文件、必须保留的视觉锚点、视觉质量硬门槛证据、渲染证据、测量偏差，以及 `pass`、`fix` 或 `reference-invalidated`。只有明确的低风险变化保持了主体、几何、层级和意义，才允许写 `intentional deviation`。任一硬门槛或明显偏差仍存在时继续修正。如果 `frontend-app-builder` 激活，遵循它的浏览器和截图对比流程。

同时写入 `docs/identity-evidence.json` 和覆盖所有 section 的 `docs/fresh-review.md`，再运行 `python3 <identity-skill>/scripts/verify_identity_run.py <project-root>`。只有命令退出码为 `0`，且逐 section 成对图片审查确实通过后，才能交付或把目标标记为完成。验证器只证明证据齐全，不能替代视觉判断。

如果实现页面主要匹配了文字主题，但没有匹配已接受参考图，即使功能正常、好看或内部一致，QA 也视为失败。

## 用户确认点

默认只在这些点暂停并请求确认：

1. 完整内容与风格 brief 完成后，生成参考图 prompt 或图片前
2. 参考图组和参考审查完成后，进入素材生成前
3. 素材拆分清单完成后，生成、复制、查找或整理新素材前
4. 已生成/已整理素材和复刻执行 brief 完成后，页面代码实现前

不要为旧的 lightweight pre-build design note 再单独增加默认确认点。它已合并进第四步复刻执行 brief。用户可以明确要求更多控制或更少暂停。

用户要求不做中间确认或默认采用推荐方案时，只跳过等待动作；仍要完整执行审查、不可覆盖参考锁、证据产出、fresh review 和确定性校验。自动继续不等于自动通过。

## Taste 处理

附带的 taste 样本是校准参考，不是强制风格。

当用户要求高质量个人网站但视觉方向有限时使用它们。如果用户提供了自己的参考图，优先使用用户图片，只用附带样本避免低质量 AI 默认效果。

不要强行使用深蓝电影感风格，除非 brief 支持。提取底层 taste 原则即可：清晰构图、受控色彩、强字体、电影感节奏、良好留白、没有无意义视觉杂物。
