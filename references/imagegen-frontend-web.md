# Identity Skill 参考图生成硬契约

`identity-skill` 的每次第二步参考图生成都必须读取本文件。

目标是精致、专业、有辨识度或 Awwwards 级时，同时读取 `visual-quality-gate.md`。本文件控制生成拓扑；视觉质量门槛判断结果是否有真实含义、完整构图和足够作者性。

本文件有两个职责：

1. 无论是否安装独立 `imagegen-frontend-web`，它都是个人网站参考图生成的强制契约。
2. 独立 skill 不可用时，它是自包含 fallback。

独立 skill 可用于补充创意词汇和一般图像方向，但如果与本文件冲突，brief 锁定、风格一致性、生成顺序、section 边界、元素预算、审查和重设计决策以本文件为准。通用规则可以扩展创意，不能放宽本契约。

不要新增用户确认点。下述 style fingerprint、render contract、anchor 检查和审查，都属于第一步 brief 确认与第二步参考图组确认之间的内部工作。

## 目录

1. 进入条件与输出 · 2. 风格指纹 · 3. Anchor-first 生成
4. Render contract · 5. 边界与预算 · 6. 质量与 anti-slop
7. 变化范围 · 8. Prompt 组装 · 9. 四向审查 · 10. Redesign-required

## 1. 进入条件与输出

只有用户确认完整的第一步 brief 后才能生成参考图：

- 站点目标、受众、定位、访客记忆点、站点形态和已确认 section 清单
- 已批准内容/占位单元、视觉方向，以及头像、logo、截图、产品和官方标记的真实素材边界
- 每个可识别人物、公司、产品、作品、出版物或项目的来源策略；确认构图前已收集可用的用户/官方素材

不要为了让画面更丰富而发明更大的站点、额外 section、证据、指标、项目、route 或交互。

每个已确认 section 生成一张独立横向网站参考图：

- 1 section -> 1 image；严格遵循已确认清单
- 不要输出竖长整页、多 section 看板、slide、contact sheet 或拼贴

每张图必须像一个聚焦、可实施的网站 section 截图。名称只写在聊天说明里，不要放进图片。

## 2. 锁定一个风格指纹

第一次生成前写一份简洁的内部 `STYLE_FINGERPRINT`，之后逐字复用。

锁定：

- 精确 wordmark/logo、唯一头像来源、裁切语言，以及摄影/插画模式
- 主色、辅色、强调色、中性色的 hex 角色；display、body、label、nav、button 字体角色
- 全局 chrome：导航位置、header 密度、active state、CTA family
- 几何：border、radius、shadow、stroke、icon 处理
- 材质和图像语言：表面、颗粒、光线、调色、裁切和 framing
- 间距/密度姿态，以及一个重复 motif 白名单和明确 blacklist

风格指纹不可变。后续 section 不得引入新配色、头像风格、wordmark 变体、字体气质、CTA 形状、圆角系统或无关材质语言。

输出与指纹冲突时重新生成，不要为了迁就模型错误而静默改写指纹。

## 3. 先生成 Anchor，再生成同一批次

先选一个 anchor section：

- 通常选 Hero
- 只有其他 section 更能定义身份、材质和图像语言时才改选

在同一次第二步运行中先生成 anchor，并在内部检查 render contract、风格指纹、焦点、预算和边界。anchor 检查不是用户确认点；失败时内部修 prompt 或 contract 并重新生成。

anchor 通过后：

- 工具支持时把 anchor 附给后续调用；否则把它实际呈现的配色、字体、chrome、材质、调色和几何写入共享块
- 其余 section 作为同一设计批次生成；并行调用只能在 anchor 通过后开始
- 所有 worker 使用完全相同的指纹、anchor 和 contract；不得各自发明设计系统

`同一批次` 指一个已锁定的第二步设计运行。工具一次只能生成一张图时，可以顺序调用。

## 4. 为每个 Section 写 Render Contract

生成前写简洁的内部 `SECTION_RENDER_CONTRACT`，包含：

- section 名称/职责和已批准可见内容
- 三秒信息、个人证据和一个由内容推导出的作者性动作
- 一个构图 anchor、一个主焦点和一个 archetype
- 0-2 个次要 anchor，以及 first -> second -> third 阅读路径
- 代码负责区域/安全区，以及图像负责区域或独立媒体槽
- 已批准的全站 shared material，以及是否已经生成
- 交互、替换和响应式 reflow 假设
- 拓扑归属：`section-specific`，或允许共享结构的准确 section 名称和几何
- 最大总 panel 数/图像 panel 数
- 留白地图、语义图形含义、重叠清单、封闭 exclusion zone、viewport payload 和禁止融合项

选择一个主要 archetype：

1. `C0 code-only`：实时文字、布局、简单几何；0 个 section 专属 raster。可以复用 1-2 个全站只生成一次的 fingerprint 材质。
2. `C1 integrated-scene`：代码 UI 叠在一张融合氛围/材质场景上，可 full-bleed 或有边界。
3. `C2 independent-media`：代码外壳加 1-3 个有独立含义和替换路径的照片、封面、截图、产品/UI mock 或单体插画。
4. `C3 scene-plus-identity`：一张融合场景，加一个有来源或 replace-later 的头像、logo 或官方产品视觉。

结尾 section 通常使用 `C0` 或 `C1`；密集产品/UI 证据通常使用 `C2`。`C0` 不代表内容不足的全屏 section 已完成：除超大字外还要有第二个内容驱动决策，否则缩短、合并或重设计。不要为了让 section 更复杂而发明新 archetype。

archetype 用于约束构图，不是让所有 section 长得相同。第三步仍负责最终素材拆分；这里负责阻止第二步生成不可实施的参考图。

## 5. 执行可复刻边界与预算

默认每个 section 只有一个主焦点和有目的的负空间。任何与焦点组同等大的空白都必须说明功能；`premium` 或 `cinematic` 不是功能。

除非用户明确批准 dense evidence-wall：

- 最多 3 个 panel：1 个主图像 panel，加 2 个小型 chip/label
- 不要堆叠 4 个以上互相覆盖的 card、window、screenshot、note 或 badge
- 不要在全站重复 dense panel-wall

全站 paper surface、grain field、scan strip 或其他 fingerprint 材质只计一次，不按 section 重复计算。shared material 是复用范围，不是第五种 archetype；section 不得发明“共享材质”逃避预算。

融合静态场景按一个拆分单元计算，但复杂度不是免费的。桌面、纸张拼贴、旅行地图、studio 或氛围背景可以包含多个共享光线、阴影和材质连续性的对象，前提是它们不需要独立交互/替换，并且仍有一个主焦点、有限主要物件组、干净文字安全区和可承受窄屏的裁切。

禁止跨归属边界融合：

- 不把 nav、headline、body、CTA、button、可编辑 label 或事实文字烘进背景
- 不合并可独立替换的媒体或身份素材；不把真人身份或官方标记生成成最终素材
- 不把连续静态场景任意切碎
- 不把独立 UI 与摄影融合；必须独立移动/reflow 的区域不能共享阴影或遮挡

为实时内容保留明确的 code-safe area。参考图要表达代码文字和 control 的位置，但图像素材不能拥有这些内容。

## 6. 不靠卡片堆达到 Awwwards 级质量

`Awwwards-level` 指完整 art direction、层级、排版、材质、图像处理、节奏和令人记住的构图，不代表更多装饰物。

通过以下方式建立辨识度：

- 构图、尺度对比、受控不对称和负空间
- 编辑式裁切、image-as-canvas 和把字体作为主要视觉材质
- 有触感的光线和已批准材质，而不是更多 panel
- 一个有意义的第二阅读细节，以及全站 rich-to-calm 节奏

每个 section 还必须通过 `visual-quality-gate.md`：三秒传达、单一主焦点、有目的元素、个人特异性、完整构图、密度上下限、有意义留白、语义图形、裁切完整性、非破坏重叠和响应式 viewport payload。

任何不能被遮挡的主体都要定义封闭 exclusion zone。prompt 使用明确区域语言，不要只写“绕开”或“从后方经过”。同一重叠错误连续两次时，终止 overlay，或重新构图，不再继续改路线。

主体是可识别产品、公司、作品、出版物、演出或项目时，优先使用用户提供或官方素材，并直接围绕真实素材构图。不要先确认更强的生成占位图，再预期锁定后换成明显不同的来源素材。生成图可提供氛围，但不能抹掉可识别主体。外部品牌证据必须连接到个人的角色、决策、过程、贡献或结果。

拒绝 AI slop：

- 用通用 AI gradient/glow、随机 blob/sphere 或渐变文字冒充高级
- filler card、假 dashboard/KPI、无意义 badge、随机 icon row
- 重复左文右卡、复制 bento、无尽 card row
- crop mark、页码、slide counter、progress rail
- 乱码 wordmark、虚构 logo、未批准主张、不可读微细节
- 没有阅读顺序、section 职责、身份或复刻目的的密度与装饰

一张有自信、材质和字体都优秀的大视觉，优于六张薄弱证据卡。

## 7. 保持在允许变化范围内

风格指纹保持固定，只允许改变：

- 构图 anchor 和背景模式
- 裁切、图像位置和图文比例
- 已批准范围内的 section 尺度/密度
- 视觉速度和负空间分布

五个以上 section 至少使用三种构图骨架。同一骨架最多出现两次；同一背景模式最多出现三次，除非用户明确批准极简方向。

rich 与 calm section 交替。不要让所有 section 都是密集、电影感、白色、暗色、卡片式或 image-as-background。

克制复用一个 motif。重复要建立身份，不能变成装饰 spam。

变化不得改变品牌身份、字体角色、全局 chrome、头像系统、配色逻辑、CTA family、材质 family 或图像调色。

## 8. 按 Contract 组装 Prompt

每个图像 prompt 由四块组成：

1. `STYLE_FINGERPRINT`：整批完全一致
2. `SECTION_RENDER_CONTRACT`：该 section 独有
3. `ANCHOR_REFERENCE`：已通过的 anchor 图，或对其实际画面的精确转录
4. `NEGATIVE_BOUNDARIES`：禁止融合、虚构内容、slop 和额外 chrome

写明横向宽高比，并要求真实网站 section 截图，不是海报或 presentation slide。

只使用已批准文案。关键实时文字要在图中体现层级和位置，但最终可编辑来源不能依赖图像文字。

没有图像生成工具时，按相同四块输出可复制 prompt。不要弱化契约，也不要因缺少独立 skill 阻塞。

## 9. 第二步交付前执行四向审查

四项全部通过前，不得把参考图组标记为 ready。

### 视觉意义审查

执行 `visual-quality-gate.md` 全部硬门槛。驳回设计不足的极简主义、无效全屏空白、装饰信息图、意外裁切、独立语义媒体互相遮挡、缺少个人作者性的品牌模仿，以及必须靠说明文字才能理解的 section。

### 一致性审查

逐图对照 fingerprint 和 anchor：

- 精确 wordmark/avatar、配色和强调色逻辑
- 字体角色、nav/header 与 CTA 身份
- 几何、材质、图像调色、间距和 motif

无法解释的漂移是失败，不是创意变化。

### 单调性审查

列出每个 section 的构图骨架、背景模式、标题尺度/位置、焦点和密度。以下情况驳回：

- 同一骨架超过两次，或所有标题尺度/位置相同
- 所有 section 使用同一背景或 panel 结构
- rich/calm 不交替
- grey-block test 让超过一半 section 失去设计

Grey-block test：在脑中把照片和 mock 换成纯灰矩形。至少一半 section 仍应通过排版、布局、色块和间距显得经过设计。

### 可复刻性审查

逐项对照 render contract：

- 一个明确焦点、预算通过、code-safe area 可用
- 实时/事实内容没有困在图像负责区域
- 独立媒体保持独立；融合场景保持静态连续
- 真人身份/官方素材保持 source 或 replace-later
- 响应式区域可以 reflow，不产生不可能的遮挡
- 代码加预估素材可以复刻，而不需要整张截图

局部失败的 section 在展示前重新生成。

## 10. 结构错误时标记 Redesign-Required

以下情况使用 `redesign-required`，不要继续做表面 prompt 修补：

- anchor 无法满足 fingerprint、焦点或预算
- 两个以上 section 违反同一结构规则，或整组一致但单调
- 跨边界融合或烘焙实时内容让参考图不可实施
- 主视觉不支持 section 职责
- 两次重新生成重复相同失败
- 视觉意义失败，即使风格一致性和可复刻性通过

执行 `redesign-required`：

1. 内部返回受影响的 render contract、variation envelope 或 anchor 选择
2. 保持已确认 brief 和视觉方向不变
3. 共享视觉系统改变时重新生成 anchor
4. 重新生成所有受影响的依赖 section
5. 重跑全部四项审查

在第二步内部完成，不新增用户确认点。只有确实必须改变用户已批准的站点形态或视觉方向时，才通过现有第二步确认/修改选项提出。

第二步之后，如果新交付素材或内容改变主要主体/来源、媒介类型、轮廓、宽高比、裁切、视觉重量、语义主体数量、焦点层级、主色块、响应式行为或个人主张，把该 section 标记为 `reference-invalidated` 并返回这里。不得用 `intentional deviation` 对抗已经失效的参考图。

父工作流接受审查后的参考图组后，使用 `references/evidence-gate.md` 把图片版本化并哈希到 `references/locked/<version>/`。不得覆盖已确认文件。

## 第二步交付契约

只展示通过审查的参考图组，以及简洁的视觉意义、一致性、单调性和可复刻性摘要。只列出不改变主体、几何、层级和含义的低风险 intentional deviation。用户未要求时，不暴露内部 prompt scaffolding。

用户在现有第二步确认点接受后，把参考图交给第三步做最终素材拆分。不要在本契约里生成最终构建素材或开始页面代码。
