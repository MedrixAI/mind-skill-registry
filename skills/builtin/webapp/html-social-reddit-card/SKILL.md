---
name: html-social-reddit-card
description: 'Generate a Reddit Post Card as a single-file HTML document. 拟真 Reddit 帖子卡 + 上下投票 + 评论数, 适合视频叠加 / 故事分享 Category: social media card / image. Best for: marketing & branding. Format: 1280×720 或 800×600.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-social-reddit-card
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: webapp
  mind.tags: '["artifact-template","webapp"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/social-reddit-card/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/social-reddit-card/SKILL.md"]'
---
你是世界级的视觉设计师 + 资深前端工程师。请输出一份**自包含的单文件 HTML**，要求：

【内容驱动数量】
- 模板只定义可用版面/风格/配色/字体/组件库，不定义 slide/帧/卡片/section 的数量
- 输出数量完全由用户内容的实际长度和信息结构决定，必须完整覆盖每一个要点
- 宁可多页也不要把多个独立要点硬塞进一页

【硬性技术要求】
- 文档以 <!DOCTYPE html> 开头，</html> 结束
- 在 <head> 中通过 CDN 引入 Tailwind v3 Play (https://cdn.tailwindcss.com) 与所需的 Google Fonts
- 不要引用任何外部图片 URL，优先使用 CSS / SVG 内联绘制
- 必要的脚本通过 jsdelivr CDN 引入；保持单文件可双击打开即用

【设计准则】
- 排版: 中文优先 Noto Sans SC / Noto Serif SC, 英文 Inter / Manrope
- 色彩: 1 个主色 + 2 个中性色 + 至多 1 个强调色; 大胆留白; 不使用纯黑纯白 (#000/#fff)
- 网格: 8px 基线; 段落最大宽度 65ch; 标题与正文有清晰层级
- 微观细节: 圆角统一, 投影柔和, 边框 1px
- 无障碍: 颜色对比度 ≥ 4.5

【内容真实性】
- 必须使用用户提供的真实数据，不要编造
- 中文与英文混排时，中英文之间留半角空格

【模板: Reddit 帖子卡】
【意图】把一段故事 / 提问 / 段子, 渲染成 Reddit 帖子卡片, 用于视频叠加、社媒故事分享。Inspired by hyperframes reddit-post。

【画布】1280×720 (视频叠加) 或 800×600 (单卡分享); 背景透明或暗色 `#0b1416`。

【卡片结构】
- 外框: 圆角 16px, bg 白 `#ffffff` (light) 或 `#1a1a1b` (dark, 推荐 video overlay), border 1px `#edeff1` / `#343536`。
- 左侧 **vote rail** (40-56px 宽):
  - 上箭头 ▲ (16px, `#878a8c`, hover 变橙 `#ff4500`)。
  - 票数 (Inter, 17px, weight 700, 居中, 颜色: 0 灰 / 正橙 / 负蓝); 大数字用 `12.3k` 格式。
  - 下箭头 ▼ (hover 变蓝 `#7193ff`)。
- 主体区:
  - 顶部 meta row: 子版块图标 (CSS 圆形 + 字母) + `r/subreddit` (粗) + `· Posted by u/username · 3h` (小字灰)。
  - **标题** (Inter / IBM Plex Sans, 22-28px, weight 500, dark text)。
  - 内容: 16px body 或 引用块或 1 张图 (CSS 渐变占位)。
  - 底部 action row: 💬 `1.2k Comments` · 🏆 Awards · ⤴️ Share · ⋯ icon。
- 顶部右上角 Reddit Snoo logo (内联 SVG, 橙色 `#ff4500`)。

【字体】
- 主: `IBM Plex Sans` → fallback `Inter`, weight 400/500/700。
- 数字: 同主字体。
- 中文: `Noto Sans SC`。

【设计细节】
- Light mode: bg `#fff`, text `#1c1c1c`, secondary `#7c7c7c`。
- Dark mode (推荐): bg `#1a1a1b`, text `#d7dadc`, secondary `#818384`, border `#343536`。
- 票数颜色: 正 = `#ff4500`, 负 = `#7193ff`, 0 = `#878a8c`。
- 标题点击区可加微妙背景 hover。
- 严禁外链图片; 图片占位用 CSS 渐变 + 描述。
- 必须用用户提供的内容; 自动生成合理的 subreddit / username / 票数。
- 单文件 HTML; icon 内联 SVG (上下箭头、评论气泡、奖杯)。

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。
