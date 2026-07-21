---
name: html-saas-landing
description: 'Generate a SaaS Landing as a single-file HTML document. 单页 SaaS 落地页 / 网页设计, 含 hero/features/social-proof/pricing/CTA Category: web prototype / mockup. Best for: marketing & branding. Format: 桌面 1440.'
license: MIT
compatibility: Requires the submit_html artifact tool.
allowed-tools:
- submit_html
metadata:
  mind.id: ai.medrix.skill.builtin.html-saas-landing
  mind.distribution: builtin
  mind.publisher: medrixai
  mind.min-harness-version: '>=1.0.0'
  mind.runtime-category: webapp
  mind.tags: '["artifact-template","webapp"]'
  mind.upstream.repo: https://github.com/nexu-io/html-anything
  mind.upstream.commit: d0efb1eaa3b65c731709981718cd5a0a0d4e8f71
  mind.upstream.path: next/src/lib/templates/skills/saas-landing/SKILL.md
  mind.upstream.import-mode: curated-fork
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://raw.githubusercontent.com/nexu-io/html-anything/d0efb1eaa3b65c731709981718cd5a0a0d4e8f71/next/src/lib/templates/skills/saas-landing/SKILL.md"]'
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

【组件库】
- 导航栏: .navbar (sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b), 滚动后加 shadow
- Hero 区: .hero (pt-24 pb-16 px-4 text-center), 大标题 text-5xl/6xl, 渐变文字 bg-gradient-to-r
- CTA 按钮: .btn-primary (bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-xl font-semibold shadow-lg hover:shadow-xl transition), .btn-secondary (border-2 border-blue-600 text-blue-600)
- 特性卡片: .feature-card (bg-white rounded-2xl p-6 shadow-sm hover:shadow-md transition), icon + 标题 + 描述
- Logo 墙: .logo-wall (flex flex-wrap justify-center gap-8 opacity-50 grayscale), 用 CSS 绘制简化 logo
- 定价卡片: .pricing-card (bg-white rounded-2xl p-8 border-2), 推荐档 border-blue-600 + 标签 "推荐"
- FAQ 手风琴: details/summary (border-b py-4), 展开时旋转箭头
- 页脚: .footer (bg-gray-900 text-gray-400 py-16), 四列链接

【推荐 CDN 资源】
- 图标: Lucide (https://unpkg.com/lucide@latest/dist/umd/lucide.js)
- 动画: Motion One (https://cdn.jsdelivr.net/npm/motion@11.12.0/dist/motion.min.js) — 滚动入场动画

【配色方案】
- 主色: #2563eb (Blue-600) — SaaS/科技
- 中性色: #f8fafc (Slate-50), #475569 (Slate-600)
- 强调色: #f59e0b (Amber-500) — CTA 高亮
- 渐变: from-blue-600 to-indigo-600

【内容真实性】
- 必须使用用户提供的真实数据，不要编造
- 中文与英文混排时，中英文之间留半角空格

【模板: SaaS Landing】
【意图】完整的 SaaS 产品落地页, 把用户内容映射到标准 sections。
【布局】
- Top nav (logo + 导航 + sign-in + 主 CTA)
- Hero (大标题 + 副标 + 双 CTA + 可视化占位)
- Logo wall (社会认证)
- Features (3-6 个特性卡, icon + 标题 + 描述)
- How it works (3 步流程, 数字 + 标题 + 描述)
- Pricing (2-3 档, 推荐档高亮)
- FAQ (details/summary 手风琴)
- Footer
【设计细节】
- 现代 SaaS 风: 大字号, 柔和渐变, glassmorphism 卡片, 滚动入场动画
- 至少处理 `md:` 断点, 移动端单栏

【输出要求】
生成完成后，调用 submit_html 工具提交最终 HTML 文档。

## anti-slop（用可执行量，禁用氛围词）
- 禁用 premium / magazine-grade / rich / futuristic / professional / 高级感 / 精美 等氛围词；改写为可执行量，例如"顶部导航 + Hero（大标题+双 CTA）+ logo 墙 + 3–6 特性卡 + 3 步流程 + 2–3 档定价 + FAQ + 页脚"。
- 不编造内容；中英文混排留半角空格。

---
> 共享基线（CDN allowlist / 设计 token / 硬性技术要求 / 响应式 / 无障碍）见 `skills/enhancements/base.md`，运行时由全局 system prompt 注入、由 `htmlassets.ValidateHTML` 强制；本 skill 仅定义版面/组件/场景差量。
