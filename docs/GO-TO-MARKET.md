# Profit Leak Detector — First Revenue Plan

Status: internal working plan; not a public offer or launch approval.

## Product

Profit Leak Detector is a lightweight, Hindi-first profit visibility tool for small shops and online sellers. The current MVP records sales, unit cost and operating expenses, then estimates gross and net profit. Data is stored in the user's browser and can be exported as CSV/JSON.

## First customer segment

Start narrower: owner-operated micro retailers and small resellers who already keep sales records but cannot quickly see product-wise contribution profit. Prefer people using notebooks or spreadsheets, not shops actively seeking a replacement for a full billing/accounting system.

Competitive reality: established products already offer billing, expense tracking, inventory and profit reports. Vyapar advertises a lifetime-free limited mobile plan as well as paid tiers; myBillBook lists broader invoicing and inventory plans. We should not compete as a billing/GST/accounting replacement. Our wedge is a quick, simple, Hindi-first profit-clarity workflow with no account, no subscription and customer-controlled local data. Verify competitor pricing/features at the time of any comparison because plans change.

Do not market it as accounting, tax, GST, inventory or audit software.

## First offer to validate

Offer a human-assisted "Profit Setup & Clarity Report":
1. Help the shop owner enter a small sample of product sales, unit costs and operating expenses.
2. Check whether the figures are complete and internally consistent.
3. Provide a simple product-wise margin and expense summary.
4. Explain which products appear to contribute the least profit, using only the supplied data.
5. Give the owner a copy of their data and explain that the result is an estimate, not a statutory account.

Suggested pilot price to test (not approved for publication): ₹299 one-time for a small setup/report. Test willingness to pay before building subscriptions. No customer outreach, payment collection or public pricing until the owner approves.

## Revenue sequence

1. Validate the one-time setup/report service with a few real shop owners.
2. Record objections, time required per setup, and whether customers would pay again.
3. Improve the free self-service tool around the repeated customer needs.
4. Only after repeat demand is demonstrated, test a paid convenience tier (backup assistance, extra reports, multi-device/cloud features only when secure and costed).
5. Consider Business/API plans only after the core workflow has proven demand.

## Free-first operating stack

- GitHub: source control, issue tracking and version history.
- GitHub Pages or another genuinely free static host: only after deployment settings and limits are checked and the owner approves publishing.
- Local browser storage and user-controlled CSV/JSON export for the MVP.
- Free office/spreadsheet tools for internal tracking.
- No paid APIs, subscriptions, ads, hosting upgrades or tools without explicit owner approval.

Free tiers can have quotas and terms; check them before relying on them. Never promise unlimited free hosting or zero operating cost without verification.

## Current MVP gaps found in the repository

- Browser-local storage only; no account, cloud sync or cross-device access.
- No transaction history or per-entry delete/edit controls.
- CSV export currently covers sales only; JSON backup includes both lists.
- JSON restore checks only that top-level arrays exist; each imported record needs validation.
- No returns/refunds, shipping allocation, payment fees, taxes, inventory valuation or multi-user access.
- The Python helper server binds to 127.0.0.1 and is for local use, not public hosting.
- README correctly warns that this is a prototype, not accounting or tax software.

## Trust, privacy and delivery rules

- Never ask customers to upload bank statements, identity documents, passwords or OTPs.
- Avoid collecting customer-identifying data; product name, quantity, selling price, unit cost and expense category are sufficient for the current use case.
- Prefer customer-owned local data and customer-controlled exports.
- Do not represent estimates as audited or tax-ready figures.
- Keep the repository free of real customer data, credentials and secrets.
- Back up before any destructive change.

## Initial validation KPIs

Track these separately; do not treat downloads or GitHub stars as revenue.

- Qualified shop-owner conversations.
- Demo requests.
- Completed setup/report sessions.
- Paid conversions and actual collected revenue.
- Delivery time per customer.
- Refunds/complaints and repeat-use rate.
- Net contribution after any transaction or delivery costs.

## Go / no-go gate

Do not build paid subscriptions or cloud accounts until:
- at least 5 target users have tried the workflow;
- at least 3 can complete the basic flow without assistance;
- at least 2 express clear willingness to pay for setup/reporting;
- import/export and calculation tests pass;
- privacy, backup and limitations are visible to users.

This is a validation target, not a claim that the targets have already been met.


## Competitive research snapshot (14 November 2026)

- Vyapar's official small-business page describes connected billing, inventory, expenses and item/bill-level profit reporting, and lists both a limited free plan and paid plans: https://vyaparapp.in/free/small-business-accounting-software
- myBillBook's official billing page lists invoicing, inventory, online-store and barcode features in its paid plans: https://mybillbook.in/s/billing-app/
- Implication: a generic shop billing app is a poor entry point. Position this MVP as a lightweight profit-clarity utility and assisted setup service for a narrow user group. Do not claim it is better than full accounting apps.
