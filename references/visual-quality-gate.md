# 视觉质量门槛（Visual Quality Gate）

目标是精致、有辨识度、专业或 Awwwards 级个人网站时，在第二步和第五步使用本文件。

这是判断契约，不是风格配方。它不强制 maximalism、minimalism、电影摄影、编辑式字体、卡片、渐变或任何固定外观；它要求每个主要视觉决策都表达真实内容，每个 section 都有作者性、完成度和可用性。

## 目录

1. 质量原则 · 2. 含义契约 · 3. 参考图硬门槛 · 4. 密度与留白
5. 证据与作者性 · 6. 裁切与重叠 · 7. 参考图失效
8. 最终构建 QA · 9. Fresh-context 审查 · 10. 回归失败模式

## 1. 质量原则

按以下顺序判断：

1. meaning：访客应理解或感受到什么
2. hierarchy：第一、第二、第三看到什么
3. evidence：什么让主张具体可信
4. composition：字体、图像、空间和动效暗示如何形成张力与平衡
5. craft：排版、裁切、材质、细节和响应式行为
6. originality：为什么这套设计不能原样贴到另一个人的网站
7. rebuildability：已批准视觉能否在不丢失想法的情况下实现

精致不能拯救缺失的含义；更多元素不能拯救弱层级；空白不能拯救未完成构图；可实施不等于好设计。

## 2. 渲染前写含义契约

每个 `SECTION_RENDER_CONTRACT` 增加：

```text
THREE_SECOND_MESSAGE: 访客三秒内应理解什么
PERSONAL_EVIDENCE: 让该 section 属于此人的、有来源证据的产物、角色、决策、结果或观点
AUTHORED_MOVE: 承担该 section 的一个可记忆构图、材质、空间或交互想法
PRIMARY_FOCAL_POINT: 第一视觉目标
SECONDARY_ANCHORS: 0-2 个辅助目标及其职责
READING_PATH: first -> second -> third
WHITESPACE_MAP: 每块大留白及其职责（focus、crop runway、motion runway、pause 或 transition）
SEMANTIC_GRAPHIC: line、node、orbit、arrow、chart 或 diagram 实际编码什么；不需要时写 none
OVERLAP_LEDGER: 每个有意重叠、层级，以及被覆盖内容为何可牺牲
EXCLUSION_ZONES: 其他 layer 不能进入的人物、面部、产品、标志、界面、caption 或证据闭合区域
VIEWPORT_PAYLOAD: desktop、ultrawide、mobile 首屏必须完整可见什么
```

这些字段暴露出没有真实想法时，不要生成。先修改概念，或合并/缩短 section。

## 3. 参考图硬门槛

只有以下门槛全部有直接视觉证据时才能标 `pass`；硬失败不能靠平均分抵消。

### A. 三秒传达

不读设计说明，审查者也能在三秒内说出 section 主体、信息和下一步想法/动作。

只能说出“未来感、编辑式、高级”或著名品牌，却说不出个人角色和 section 含义时失败。

### B. 单一主焦点

缩略或轻微模糊时，一个元素应立刻胜出，辅助 anchor 最多两个。

大标题、hero 照片、浮动 UI、CTA 和装饰图表同时争夺同等权重时失败。

### C. 有目的的视觉元素

每个主要 image、panel、line、icon、label、texture 和 motif 至少承担一个明确职责：身份、证据、导航、解释、交互、与概念相关的氛围或节奏。

唯一理由只是“看起来像设计过”“增加科技感”或“填空间”时，删除或重设计。

### D. 个人特异性

至少有一个内容驱动决策，在换成另一个人的名字后会变得错误或无意义。

精致品牌模仿、通用作品集和只提供氛围、看不出个人角色/判断/过程/作品/结果的 section 都失败。

### E. 完整构图

字体、图像和空间必须组成同一构图，而不是割裂的左右两半。阅读路径应在 section 内结束，或明确交给下一 section。

意外失衡、孤立 caption、脱节 control、未完成角落或像掉到 fold 下方的内容都失败。

### F. 响应式完整性

焦点主体、关键文案和有意义 control 在 desktop、ultrawide、mobile 都不能意外裁切、碰撞、缩到不可读或隐藏证据。

不同 viewport 可以使用不同裁切，但必须写入 contract。

### G. 可复刻性

继续满足已有代码/图像/身份边界。视觉质量不能为不可拆分开脱；可复刻也不能为弱视觉想法开脱。

## 4. 密度与留白

密度同时有上限和下限。

### 密度上限

继续执行素材和 panel 预算。驳回重复卡片堆、同权重证据墙、装饰簇，以及同一 viewport 中多个独立故事。

### 密度下限

`C0 code-only` 表示代码是正确媒介，不表示只有超大字和分隔线的空全屏已经完成。

稀疏 section 只有在排版、比例、对齐、色域、顺序或动效暗示形成完整作者性机制时才通过。除“把标题放大”外必须有第二个设计决策；内容支撑不起时缩短、合并或换概念。

执行移除测试：

- 在脑中移除 headline 文案
- 只剩空画布、divider 和通用 label：设计不足
- 空间系统、证据结构、视觉隐喻或交互想法仍可读：克制是有意图的

### 留白地图

任何连续空白只要视觉面积等于或大于主焦点组，都必须说明功能：

- 聚焦主主体
- 图像移动/响应式裁切的 crop runway
- 明确交互的 motion runway
- 两个高强度 section 之间的叙事停顿
- 明确指向下一内容的方向转场

固定高度容器未填满、carousel 没占满轨道、内容意外落到 fold 下方或布局没有 counterweight 造成的留白都失败。`premium` 和 `cinematic` 不是留白功能。

不要靠 filler 修死空白；重新构图、调整尺寸、缩短或合并。

## 5. 证据、信息图与作者性

### 来源优先

section 涉及可识别产品、公司、作品、出版物、演出或项目时，优先使用真实的用户/官方素材。生成素材可建立氛围或辅助场景，但不能为了避免伪造而抹掉可识别主体。

外部品牌证据必须回到个人：说明或视觉编码其角色、决策、过程、贡献或结果。否则只是精致品牌页，不是个人网站。

### 图形必须编码含义

每个 diagram、orbit、node system、curve、grid、map 或 arrow 都要说明：

- 每个元素代表什么
- 位置、大小、方向、连接或顺序代表什么
- 访客从关系中学到什么

回答不出来就删除图形，或改成诚实的氛围处理。不要把装饰工程线冒充信息设计。

### 每个 Section 一个作者性动作

要求一个由概念支撑的视觉动作，而不是一堆 signature component。例如：有意义的裁切序列、从作品推导的空间隐喻、把证据物变成导航、揭示真实系统的 diagram，或反映个人过程的字体行为。

动作必须来自内容；把流行处理贴到无关内容上不算。

## 6. 裁切、序列与重叠

### 裁切完整性

为每张重要图像记录 subject-safe box 和允许裁切。

硬失败：

- 人物、产品、icon、作品或界面的识别部分被意外切掉
- 横向素材放进隐藏识别信息的容器
- 首屏出现没有明确交互提示的半张 card/caption
- mobile 裁切移除了图像存在的证据理由

横向 carousel 首屏默认展示一个完整主要项目，加一个有意图的后续预览。只有尺寸差异表达层级、基线仍明确时才允许不等大卡片。

### 语义重叠

独立语义主体默认不能互相遮挡，包括不同品牌、项目、产品截图、人物、作品和证据项。

重叠只有在 `OVERLAP_LEDGER` 写清以下内容时才通过：

- 主体与从属主体
- 被覆盖的可牺牲区域
- 重叠如何改善含义，而不只是增加层次
- mobile 如何分离或 restack

明亮 UI 遮住焦点照片、两个品牌竞争同一 hero、caption/control 漂在无关证据上方时失败。

### 闭合 Exclusion Zone

每个必须完整可见的主体都要用明确区域或 contour 定义闭合 exclusion zone。其他 code、image、line、marker、shadow、mask 和 decoration 都不能进入。

使用确定性 prompt，例如 `all route graphics remain entirely left of the person-safe boundary` 或 `no overlay enters the sign rectangle`。不要依赖 `route around`、`pass behind`、`avoid the subject` 等含糊表达。

同一重叠错误重复两次后，不要继续在同一拓扑中改路线。让 overlay 在 exclusion zone 前结束，改用颜色/顺序表达关系，或重新构图。

## 7. 参考图失效

后续素材或内容改变以下任一项时，已确认参考图失效：

- 主要主体或来源
- 图像类型、轮廓、宽高比、裁切或视觉重量
- 独立语义主体数量
- 焦点层级或阅读路径
- 明暗平衡或主色块
- 必要响应式 reflow
- 个人主张、角色或证据

标记 `reference-invalidated`，返回第二步重新生成/构图后才能实现。不能把这些变化写成 `intentional deviation` 后继续使用旧参考图。

低风险偏差仅包括文案修正、无障碍 control 重建、微小间距调整，以及不改变主体、几何、层级和含义的实现细节。

## 8. 最终构建视觉 QA

门槛执行两次：参考图一次，放进连续滚动环境的最终渲染再一次。

最终 QA 必须包括：

- 参考 viewport 下的独立 section 截图
- 显示前后 section 转场的连续滚动截图
- desktop、ultrawide、mobile 截图
- thumbnail/blur 焦点测试
- 首屏 viewport payload
- subject-safe 裁切
- overlap 与 z-index
- 闭合 exclusion zone
- 对照实际尺寸检查 whitespace map
- 个人证据
- `evidence-gate.md` 要求的每个 section/viewport 参考图与渲染图持久化对照；抽查不能证明全站

以下情况即使几何匹配也自动失败：

- 无效全屏空白
- 不完整或意外裁切的主要媒体
- 多个同权重第一焦点
- 没有可读关系的装饰信息图
- 独立语义媒体互相遮挡
- 著名品牌比网站主人更显眼
- 素材变化让参考图失效

fidelity ledger 必须为每个硬门槛记录 `pass`、`fix` 或 `reference-invalidated`。`Intentional deviation` 只适用于参考图仍有效且理由具体的低风险变化。

## 9. Fresh-Context Art Director 审查

Awwwards 级或专业质量目标，在环境支持独立 reviewer/thread 时，参考图组完成后和最终构建后各做一次 fresh-context 审查。

只给审查者：

- 已确认内容/身份 brief
- 目标质量线
- 原始图像或页面截图

不要提供生成者自评、疑似缺陷、计划修复或实现说明。

要求审查者报告：

- 三秒信息
- 第一、第二、第三焦点
- 有意义与无效留白
- 证据和个人作者性
- 意外裁切、碰撞或重叠
- 最强和最弱 section
- 每个 section 的 `pass`、`fix` 或 `redesign-required`

自评分不能覆盖 fresh-context 硬失败。重新生成或构图，再审查。

把审查保存到 `docs/fresh-review.md`，覆盖每组 section 对照，并在交付前运行 `evidence-gate.md` 的确定性验证器。缺少 screenshot、ledger、review 或 manifest 时为 `not verified`，即使 reviewer 看过临时浏览器状态也一样。

## 10. 回归失败模式

### 设计不足的极简主义

症状：大 headline、divider、通用 label，占用大部分 viewport 的无效空白；移除文案后设计消失。

修复：增加内容驱动的空间/交互机制，重新平衡，或缩短/合并。不要用装饰卡片填充。

### 失衡的展示轨道

症状：单张媒体卡很好，但尺寸层级含糊、基线不齐、caption 被切、drag affordance 弱，下一 section 前有死空白。

修复：把轨道和 viewport payload 作为一个构图重设计；完整展示主要项目，并留下有意图延伸。

### 装饰性信息图

症状：orbit、line、node 或 label 暗示系统却不编码关系；低对比和大空场让图形像未完成。

修复：建模并编码真实关系，或删除 diagram，使用诚实氛围处理。

### 替换来源素材但不重构

症状：生成抽象占位被官方摄影或产品界面替换，但原裁切、宽高比、文字位置和参考图确认状态不变。

修复：标记 `reference-invalidated`，返回第二步围绕真实素材重设计。

### 语义碰撞

症状：两个品牌/项目共用一个 hero；明亮界面遮住摄影主体；多个独立故事无层级竞争。

修复：选择一个主故事；把另一个拆成序列或独立 section；或定义有明确层级的非破坏关系。

## 接受标准

只有所有硬门槛通过、没有回归失败模式、且不依赖解释说明也能感到具体、完整、有含义时，才能接受 section。

只有所有 section 形成同一个作者性世界、强度和留白构成有意图的滚动叙事、且个人比借来的风格或外部品牌更令人难忘时，才能接受全站。
