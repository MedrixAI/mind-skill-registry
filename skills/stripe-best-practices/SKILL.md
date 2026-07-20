---
name: stripe-best-practices
description: Guides Stripe integration decisions — API selection (Checkout Sessions vs PaymentIntents), Connect platform setup (Accounts v2, controller properties), billing/subscriptions, Treasury financial accounts, integration surfaces (Checkout, Payment Element), migrating from deprecated Stripe APIs, and security best practices (API key management, restricted keys, webhooks, OAuth). Use when building, modifying, or reviewing any Stripe integration — including accepting payments, building marketplaces, integrating Stripe, processing payments, setting up subscriptions, creating connected accounts, or implementing secure key handling.
metadata:
  mind.id: ai.medrix.skill.stripe-best-practices
  mind.distribution: marketplace
  mind.market-primary: business-operations
  mind.market-categories: '["business-operations"]'
  mind.marketplace-summary: stripe-best-practices (stripe)
  mind.presentation: '{"default_locale":"en-US","locales":{"en-US":{"description":"Guides Stripe integration decisions — API selection (Checkout Sessions vs PaymentIntents), Connect platform setup (Accounts v2, controller properties), billing/subscriptions, Treasury financial accounts, integration surfaces (Checkout, Payment Element), migrating from deprecated Stripe APIs, and security best practices (API key management, restricted keys, webhooks, OAuth). Use when building, modifying, or reviewing any Stripe integration — including accepting payments, building marketplaces, integrating Stripe, processing payments, setting up subscriptions, creating connected accounts, or implementing secure key handling.","starter_prompts":["Help me with stripe best practices. Start by asking for the business goal, stakeholders, available inputs, constraints, and desired decision or deliverable, then complete the workflow.","Apply stripe best practices to the material I provide, identify the most important findings, risks, and evidence gaps, and produce a decision-ready result.","Review my existing stripe best practices work, correct weak assumptions or missing details, and return an improved version with clear next actions."]},"zh-CN":{"description":"指导 Stripe 集成决策，包括支付 API、Connect、订阅、Treasury、集成界面、弃用 API 迁移，以及密钥、Webhook 和 OAuth 安全实践。","starter_prompts":["请帮我完成stripe best practices。先询问业务目标、利益相关者、现有输入、约束以及需要支持的决策或交付物，然后完成整个流程。","请对我提供的材料开展stripe best practices，找出最重要的发现、风险和证据缺口，并输出可用于决策的结果。","请审查我现有的stripe best practices成果，修正薄弱假设和遗漏细节，并给出改进版本及明确的后续行动。"]}}}'
  mind.publisher: medrixai
  mind.upstream.repo: https://github.com/stripe/ai
  mind.upstream.commit: f915ccf3cc13faae9b18ce2e734156e181db20da
  mind.upstream.path: skills/stripe-best-practices/SKILL.md
  mind.upstream.import-mode: exact-snapshot
  mind.upstream.license: MIT
  mind.upstream.evidence-urls: '["https://github.com/stripe/ai/blob/f915ccf3cc13faae9b18ce2e734156e181db20da/LICENSE", "https://raw.githubusercontent.com/stripe/ai/f915ccf3cc13faae9b18ce2e734156e181db20da/skills/stripe-best-practices/SKILL.md"]'
license: MIT
---

Latest Stripe API version: **2026-06-24.dahlia**. Always use the latest API version and SDK unless the user specifies otherwise.

If you do not have a Stripe account, you can call a CLI command to generate working API keys with no registration required. You can install the Stripe CLI (`npm i -g @stripe/cli`) and run the command `stripe sandbox create` to get started.

API key default: Always recommend a [restricted API key (RAK)](https://docs.stripe.com/keys/restricted-api-keys.md) (`rk_` prefix) over a secret key (`sk_` prefix).

## Integration routing

| Building… | Recommended API | Details |
| --- | --- | --- |
| One-time payments | Checkout Sessions | <references/payments.md> |
| Custom payment form with embedded UI | Checkout Sessions + Payment Element | <references/payments.md> |
| Saving a payment method for later | Setup Intents | <references/payments.md> |
| Connect platform or marketplace | Accounts v2 (`/v2/core/accounts`) | <references/connect.md> |
| Usage-based billing (new integration) | Metronome | <references/billing.md> |
| Subscriptions or recurring billing | Billing APIs + Checkout Sessions | <references/billing.md> |
| Sales tax, VAT, or GST compliance | Stripe Tax + Registrations API | <references/tax.md> |
| Embedded financial accounts / banking | v2 Financial Accounts | <references/treasury.md> |
| Security (key management, RAKs, webhooks, OAuth, 2FA, Connect liability) | See security reference | <references/security.md> |

Read the relevant reference file before answering any integration question or writing code.

## Critical rules

- *Never include `payment_method_types` in any Stripe API call*, with one exception: Terminal (in-person payments) integrations must pass `payment_method_types: ['card_present']` on the PaymentIntent. For all other integrations, omit this parameter entirely to enable dynamic payment methods, which enables you to configure payment method settings from the Dashboard and dynamically display the most relevant eligible payment methods to each customer to maximize conversion. To customize which payment methods you accept, use [`payment_method_configurations`](https://docs.stripe.com/payments/payment-method-configurations.md) or `excluded_payment_method_types` instead of `payment_method_types`.

## Key documentation

When the user’s request does not clearly fit a single domain above, consult:

- [Integration Options](https://docs.stripe.com/payments/payment-methods/integration-options.md) — Start here when designing any integration.
- [API Tour](https://docs.stripe.com/payments-api/tour.md) — Overview of Stripe’s API surface.
- [Go Live Checklist](https://docs.stripe.com/get-started/checklist/go-live.md) — Review before launching.
