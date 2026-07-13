# 品味校准（Taste Calibration）

这些样本反映了当前对高质量个人网站的一种偏好方向。当用户给出的视觉方向很少时，用它们来做校准。当用户提供了另一种清晰的风格时，不要硬套它们。

## 偏好原则（Preferred Principles）

- 干净、高端、受控
- 有足够的视觉想象力，但不至于混乱
- 强排版与清晰的层次
- 有意义的图像，而非凑数的装饰
- 有目的的留白与经过设计的节奏；不要把空白直接等同于高级
- 各 section 间一致的配色
- 交互想象通过布局暗示，而非随意的 UI 杂乱
- 避免平庸的模板与显眼的 AI 科技视觉默认套路
- 每个 section 至少有一个由内容推导出的作者性设计动作
- 有来源支撑的个人证据，应比借来的品牌或风格更令人难忘

## 样本集：quiet-cinematic-blue（Sample Set: quiet-cinematic-blue）

路径：

- `references/taste-samples/quiet-cinematic-blue/01-hero.png`
- `references/taste-samples/quiet-cinematic-blue/02-about.png`
- `references/taste-samples/quiet-cinematic-blue/03-writing.png`
- `references/taste-samples/quiet-cinematic-blue/04-shoot.png`
- `references/taste-samples/quiet-cinematic-blue/05-build.png`
- `references/taste-samples/quiet-cinematic-blue/06-contact.png`

用户评价：

- 安静、单一色调的电影式节奏
- 干净且高端
- 强烈的色彩一致性
- 不杂乱

适用于：

- 个人站点应当给人安静、电影感、克制、以个人 IP 为驱动的感觉时
- 用户想要一个干净但令人难忘的站点时
- 站点需要在多个 section 上保持一个统一的视觉世界时

提取：

- 单色或近单色的配色纪律
- 大尺度的编辑式排版
- 强烈的、以图像为主导的构图
- 平静的间距与低杂乱度
- 逐个 section 的连续性

不要盲目照抄：

- 那个确切的蓝色配色
- 那个确切的人物或影像
- 如果用户的内容需要更安静的层次，就别用超大号排版

## 样本集：multi-element-hero（Sample Set: multi-element-hero）

路径：

- `references/taste-samples/multi-element-hero/01-collage-hero.png`

用户评价：

- hero 很好
- 元素很多但不乱

适用于：

- 用户拥有很多身份碎片、项目、媒体、帖子或作品时
- hero 应当给人一个个人世界或证据墙的感觉时

提取：

- 当保留一个主导层次时，多个内容作品可以奏效
- 拼贴需要一个清晰的焦点与受控的色彩强调
- 导航与 CTA 必须在繁忙的场景之上保持可读

避免：

- 让每个物件都平等地相互争夺注意力
- 在多个卡片里重复同一个内容概念
- 让 hero 难以扫读

## 样本集：dark-editorial（Sample Set: dark-editorial）

路径：

- `references/taste-samples/dark-editorial/01-writing-index.png`
- `references/taste-samples/dark-editorial/02-build-timeline.png`
- `references/taste-samples/dark-editorial/03-shoot-cinematic.png`

用户评价：

- 优雅 / 暗色编辑式风格
- 留白平衡得好
- 强烈的高端设计感

适用于：

- 用户想要一个编辑式、档案感、或暗色高端的个人站点时
- 站点包含写作、项目、日志或创作者记录时

提取：

- 暗色带纹理的表面
- 克制的暖色强调
- 编辑式侧栏与索引标记
- 大号排版配稀疏的辅助细节
- 电影感的负空间

避免：

- 让它太晦涩或不可读
- 添加没有目的的装饰性标签
- 过度使用纹理直到布局显得脏乱

## 负面样本（Negative Samples）

路径：

- `references/taste-samples/negative/01-letter-like-duplicated-copy.png`
- `references/taste-samples/negative/02-overdense-chaotic.png`

用户评价：

- 第一个负面样本：有点乱，左右两侧的文案相互重复，右侧感觉不清晰，像在写一封信
- 第二个负面样本：密集元素太多，视觉上很混乱

避免：

- 说同一件事的重复文案块
- 目的不清的侧面板
- 太多相互争夺的内容群组
- 不为 section 职责服务的装饰性便签/卡片
- 破坏阅读顺序的密度

## 真实个人网站测试中的回归案例

以下是语义失败模式，不是对某种视觉风格的禁令。

### 设计不足的极简主义

症状：

- 超大标题、分隔线、通用标签和大面积未使用的 viewport
- 去掉标题文案后，不再剩下空间系统、证据结构、视觉隐喻或交互想法
- section 高度来自默认全屏设置，而不是内容需要

不要靠添加凑数卡片修复。增加一个由内容推导出的设计机制，重新平衡或缩短 section，或者与相邻 section 合并。

### 失衡的展示轨道

症状：

- 单张项目图很好，但卡片层级含糊
- 卡片基线和 caption 像被意外裁切
- 拖动提示与媒体轨道脱节
- 展示轨道和下一 section 之间存在大块无效空白

把媒体、轨道、首屏载荷、交互提示和下一 section 的衔接作为同一构图来设计。首屏应完整展示一个主要项目，并留下有意图的后续延伸。

### 装饰性信息图

症状：

- 轨道、节点、网格或工程线暗示某个系统，却没有编码真实关系
- 位置、尺度、连接和方向没有可读含义
- 低对比度几何只剩空洞背景，而不是信息

要么建模并编码真实关系，要么移除图表，改用诚实的氛围处理。

### 替换来源素材但不重构构图

症状：

- 抽象生成占位图被官方摄影或真实产品界面替换
- 原有宽高比、裁切、文字位置、层级和参考图确认状态完全不变

旧参考图已经失效。围绕真实素材重新构图，并在实现前确认新的参考图。

### 语义碰撞

症状：

- 两个品牌、项目、人物或产品故事共用一个 hero，却没有主叙事
- 明亮界面窗口遮挡焦点照片或作品
- 独立媒体仅为了制造层次而互相覆盖

选择一个主故事；把另一个拆成后续序列或独立 section；或者明确非破坏性的层级和移动端重排规则。

### 品牌奇观压过个人作者性

症状：

- 著名公司、产品或 campaign 比网站主人更令人难忘
- 官方素材承担了全部视觉冲击，而个人贡献只剩泛化文案

保留真实证据，但要把它清楚连接到个人的角色、决策、过程、贡献或结果。

## 如何应用品味（How To Apply Taste）

在生成参考图之前，先判定哪个方向适合用户的 brief：

- quiet cinematic：一个强烈的色彩世界，以图像为主导，平静而高端
- multi-element hero：作品丰富但受控，适用于创作者/项目繁多的个人品牌
- dark editorial：档案/索引/日志感，克制的强调色，强排版
- user-provided style：把用户当前的参考置于这些随附样本之上优先考虑

然后把品味翻译成具体的图像约束：

- 配色
- 排版气质
- section 节奏
- 图像处理
- 密度层级
- 构图锚点
- 需要避免什么

还要为每个 section 记录：

- 三秒内必须传达的信息
- 个人证据
- 一个作者性设计动作
- 焦点层级与阅读路径
- 留白承担的功能
- 图表或装饰几何的语义
- 裁切安全的 viewport 载荷与重叠规则

使用 `visual-quality-gate.md` 做通过/失败判断。品味样本只能校准可能的视觉世界，不能让表达薄弱或设计未完成的 section 变成合格。
