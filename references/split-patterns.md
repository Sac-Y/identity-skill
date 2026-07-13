# 拆分模式：确定性先例（Split Patterns）

只有执行 `reference-asset-splitter.md` 的固定优先级和三轴裁决后，才能使用这些先例。匹配结构问题，不匹配视觉风格。先例不能覆盖真实性、语义内容或明确行为。

## 目录

- 示例 1-3：装饰簇、内容 panel、项目卡
- 示例 4-8：头像、vignette、产品 mock、diagram、零素材
- 示例 9-12：地图、full-bleed 照片、桌面场景、封面网格
- 示例 13-15：必须重设计的参考图
- 回归矩阵与最终检查

## 示例 1——Hero 融合装饰卡片簇

参考：左侧是实时 headline 和 CTA；右侧是蓝色形状、dot field、绿色曲线和五张共享阴影/纸张纹理的重叠装饰卡。

- **A 轴**：一个静态装饰组件；卡片没有独立含义、替换、reflow 或行为。
- **B 轴**：raster；拼贴有不规则印刷纹理、跨卡遮挡和共享光线。
- **C 轴**：一个 `integrated-scene`，命名为 `hero-right-world`。
- **Code-native**：导航、headline、角色/地点文案、CTA、社交链接、证据行。
- **正确**：1 个生成素材。
- **错误**：仅因对象可识别，就把卡片、蓝色形状、点和曲线拆成 8-11 个文件。

装饰世界中的“数据感数字”不会自动改变裁决：未批准内容改为不可读抽象 bar/mark；已确认事实用代码叠加；只有 brief 明确要求独立 click/replace/responsive 时才拆。共享阴影阻止拆分时使用 `redesign-required`。

默认交互说明：`右侧按静态融合场景处理；其中不承载可维护数据。`

## 示例 2——彩色 Panel 内的实时内容卡

参考：蓝色 panel 包含头像行、Education 卡、Focus Areas、Timeline 和 Working Location；右侧是奶油色文字栏。

- **A 轴**：实时 panel 内容保持代码区域；头像是身份来源；Education 卡内部 crest、校园线稿/印刷、纸张材质和局部构图是一张融合视觉。
- **B 轴**：panel、列表、timeline、label、icon、dot、简单地图线和右侧文字为 code-native；头像为 raster source；Education 为 hybrid，一张 `education-card-art` 保留完整卡片视觉，可维护文案在安全区用代码叠加。
- **C 轴**：`headshot` 是 `independent-media`；`education-card-art` 是 `composite-foreground`。
- **正确**：2 个素材：头像加一张完整 Education 视觉卡。
- **错误**：把整个蓝 panel 做成图片；拆开 crest 与校园印刷；把教育/timeline 文案烘进像素；把每个小 icon raster 化。

原因：panel 是布局，不是图片。一个 raster 成分只让该卡变成 hybrid，不会让整个 panel 变成图片。

## 示例 3——嵌入产品媒体的项目卡

参考：三张作品卡包含已确认项目文案，以及桌面截图、手机截图、简单 flow diagram 和搜索结果截图。

- **A 轴**：项目文案是实时语义内容；桌面、手机和搜索截图是三个独立媒体槽。
- **B 轴**：卡片外壳/文案为 code-native；三张密集截图为 raster；boxes-and-arrows flow 用 code-native SVG。
- **C 轴**：3 个 `independent-media`。
- **正确**：3 个通常为 `source` / `replace-later` 的截图素材。
- **错误**：整卡导出海报；合并所有截图；生成虚构截图冒充真实项目证据。

只有用户明确把卡定义为不可编辑海报时，才提供整卡方案。缺少交互说明本身不构成歧义。

## 示例 4——真实头像叠简单几何

参考：真人头像叠在蓝灰色块、细条纹矩形、黑色 quote card、headline 和 tag chip 上。

- 头像有独立身份来源；其他都是实时内容或简单装饰。
- 头像为 raster source；色块、条纹、quote card、tag、underline 为 code-native。
- **正确**：1 个 `source` / `replace-later` 的 `independent-media`。
- **错误**：把头像、quote 文案和色块合成 Hero screenshot，或把每个几何块导出成素材。

真人面部不可逆地画进生成场景时，转到示例 14。

## 示例 5——摄影式角落 Vignette

参考：实时 process card 和红 ribbon 旁边是一组共享材质、遮挡和阴影的 notebook、pen、paper grain、coffee stain 与装饰手写。

- process card/ribbon 为 code-native；角落摄影为 raster。
- **正确**：1 个透明或干净底的 `composite-foreground`：`notebook-vignette`。
- **错误**：把 process card 做成图片，或拆开 notebook、pen、stain、handwriting。

手写只能无语义；需要承载批准文案时改用代码，或重设计 vignette。

## 示例 6——代码卡片中的密集产品 Mock

参考：三张项目卡分别嵌入 calendar app、study assistant/phone、kanban tracker，旁边是已确认项目文案。

- 每个 mock 代表不同项目，必须独立来源/替换。
- mock 为 raster；shell、彩色 panel、label、Problem/Approach/Signal 和 CTA 为 code-native。
- **正确**：3 个 `source` / `replace-later` 截图；只有 brief 明确它们是虚构概念替身时才能生成。
- **错误**：合并三个 UI、烘焙项目文案，或用空通用 box 替代参考图的密集 UI 核心。

## 示例 7——技能列表旁的简单循环图

参考：五行技能列表旁是一块 teal panel，包含点阵和 Discover → Define → Decide → Deliver 圆环。

- 全部内容实时且响应式，无 raster 来源。
- list、icon、divider、panel、dot、arrow、ring、label 均在 code whitelist。
- **正确**：0 个图片素材；循环用 HTML/SVG。
- **错误**：rasterize icon、导出 panel、或整页做背景图。

只有参考图包含材质不规则手绘、印刷磨损或绘画细节时才改变结果，不能因为 diagram 看起来密集就用图片。

## 示例 8——零素材 Contact 页面

参考：headline、三个 contact button、纯色色带、简单装饰和空头像框。

- 当前可见元素全部 code-native；缺失头像是身份槽。
- **正确**：0 个生成素材；只有设计确实要求头像时才标 `replace-later`。
- **错误**：为了避免报告 0 素材而发明装饰图。

## 示例 9——纹理地图上的独立照片

参考：三张真实旅行照片位于带不规则 contour、route、pin 和 stamp 的纸张地图上，右侧是实时地点列表。

- 照片是独立 source；地图纹理/contour/stamp 是一个静态融合平面；文字实时。
- 照片和地图为 raster；白框、shadow、heading、地点列表和简单 route/pin overlay 为 code-native。
- **正确**：1 个 `integrated-scene`（`travel-map`）加 3 个 `independent-media`，共 4 个素材。
- **错误**：因照片与地图重叠就合并；拆开地图纹理/contour/stamp；用平面 CSS 近似材质地图。

照片节点先被真实性与语义独立性锁定，所以视觉重叠不会让它们融合。

## 示例 10——电影式 Full-Bleed 结尾

参考：通用夜间海岸村落氛围铺满 section；上方是 title、email、button、社交 link 和 copyright。

- 环境图是一张静态 field；所有沟通内容实时。
- **正确**：1 个 `background`；如果画面声称真实个人地点/事件，改用 `source`。
- **错误**：把 title/email 烘进照片，或把山、村、海、天拆成层。

## 示例 11——带真实插槽的艺术化桌面场景

参考：编辑式 desk world 包含纸张、coffee cup、notebook、pen、plant、scrap；其上有干净头像槽和 browser-work 槽，实时 headline/CTA 位于预留负空间。

- 桌面道具是一张静态融合组件；头像和真实作品截图有独立真实性/替换边界。
- 桌面为 raster；头像/作品截图为 raster source；copy、button、browser shell、portrait frame 和各插槽局部 shadow 为 code-native。
- **正确**：1 个 `integrated-scene` 加 2 个 `independent-media`，共 3 个素材。
- **错误**：拆分每个桌面道具；把真人头像或仓库事实/链接烘进生成场景。

参考图必须给两个真实插槽干净边界；跨对象光线/反射/遮挡使其不可分时使用 `redesign-required`。

## 示例 12——全景封面加照片网格

参考：一张有边界的 panoramic cover 位于三张独立项目/旅行照片卡上方，周围是实时文字。

- cover 和三张照片是四个有独立含义的媒体槽。
- 四张照片为 raster source；title、eyebrow、body、icon、column、divider、timeline、CTA 为 code-native。
- **正确**：4 个 `independent-media`。cover 有边界且不是代码内容后的 edge-to-edge surface，因此不是 `background`。
- **错误**：把三张照片合成 strip，或因为 cover 参与布局就称它 code-native。

## 示例 13——带跨边界效果的交互卡

参考：四张卡必须独立 hover/open，却互相重叠并共享投影、glass reflection、torn-paper edge 和跨卡前景物。

- **冲突**：交互要求四个独立边界；fusion graph 要求一个连通 raster 组件。
- **正确**：`redesign-required`。
- **最小重设计**：保留配色、拼贴 motif、材质和不对称；移除跨卡遮挡/反射；每张交互卡拥有自己的 raster core 和局部 shadow，外壳由代码负责；需要时增加独立静态氛围层。
- **错误**：切成四张有接缝风险的图，或保留死图加 invisible hotspot。

## 示例 14——真人身份融合进生成场景

参考：人物面部被画进生成房间；plant 遮住肩膀、场景光反射到脸上、手写图形跨过头像边界。

- **冲突**：真实性/替换要求独立真人头像；融合要求头像与房间保持一个 raster 组件。
- **正确**：`redesign-required`。
- **最小重设计**：保留房间、光线气质、裁切和个人风格，但建立没有跨边界遮挡的干净头像框/切口；房间为 `background` / `integrated-scene`，头像为 `independent-media`。
- **错误**：生成假真人最终头像；从低清参考图抠脸；用 CSS filter 掩盖接缝。

## 示例 15——实时文案画在响应式物理场景中

参考：headline、项目事实和 CTA 被手写在摄影桌面场景的斜纸上；移动端要求纸张重排、headline 改变换行。

- **冲突**：语义和响应式要求实时独立内容；透视、材质和共享阴影让它们无法与 raster 场景分离。
- **正确**：`redesign-required`。
- **最小重设计**：生成场景保留空白装饰纸和干净负空间，把真实 headline/fact/CTA 移到代码 overlay 或相邻代码卡；保留 paper-desk art direction。
- **错误**：把已确认文案烘进图片；分别用桌面/移动截图；用平面代码 box 近似整个场景。

## 回归矩阵

| 示例 | 预期结果 |
| --- | --- |
| 1 | 1 integrated scene |
| 2 | 1 头像 + 1 完整 Education 视觉卡；实时 panel 用代码 |
| 3 | 3 independent media；项目卡用代码 |
| 4 | 1 independent portrait source |
| 5 | 1 composite foreground |
| 6 | 3 independent product screenshots |
| 7 | 0 assets |
| 8 | 0 generated assets；可选空 replace-later 槽 |
| 9 | 1 integrated scene + 3 independent photos |
| 10 | 1 full-section background |
| 11 | 1 integrated scene + 2 independent real inserts |
| 12 | 4 independent media |
| 13 | redesign-required：interaction 与 fusion 冲突 |
| 14 | redesign-required：authenticity 与 fusion 冲突 |
| 15 | redesign-required：semantics/reflow 与 fusion 冲突 |

## 最终检查

1. 按 authenticity → semantics → interaction → medium → fusion → budget → taste 执行。
2. 先判断语义区域，再枚举可见对象。
3. 严格使用 code whitelist；混合区域使用 `hybrid`。
4. 没有高优先级边界时，静态 fusion graph 连通分量保持粗颗粒。
5. 真实独立媒体即使与场景重叠也保持分离。
6. 不要为每个 Hero 或缺少交互说明的情况自动生成备选。
7. 只有真实未决行为才给备选；不可能边界使用 `redesign-required`。
8. 如实报告 0 素材，并逐页展示。
