# PRD: ReconPilot (MVP)

## 1. Problem
Automated matching clears straightforward transactions, but a long tail of reconciliation **breaks** still needs manual investigation. Analysts compare fields across ledger, bank and payment systems, interpret rules, search past cases and coordinate with other teams. The work is slow, repetitive and depends on individual expertise. Recurring root causes are rarely fixed upstream.

**Core question:** how can we investigate breaks and recommend resolutions automatically, while keeping humans in control of every decision?

## 2. Users
- **Primary:** reconciliation and operations analysts; middle/back-office and finance operations teams; exception-management teams.
- **Secondary:** operations managers; risk and compliance (audit trail); technology/data owners (upstream fixes).
- **Initial target customers (positioning):** Indian financial institutions: banks, co-operative banks, NBFCs and payment operations teams reconciling internal ledgers, bank statements and payment-gateway settlements for UPI, NEFT and IMPS. The Indian Banking sample dataset demonstrates this use case.
- **Later segments:** asset managers, fintechs, payment companies, brokers, custodians (the multi-currency Nexora dataset shows the general engine).

## 3. Goals / non-goals
| Goals (MVP) | Non-goals (MVP) |
|---|---|
| Deterministic 3-way reconciliation with explainable breaks | Executing financial postings or corrections |
| Root cause + evidence + similar cases + next best action | Autonomous approval of resolutions |
| Simulate resolution alternatives before deciding | Trained ML / external LLM dependency |
| Human approval, rejection and investigation with full audit | Multi-tenant auth, SSO, entitlements |
| Detect recurring patterns and recommend upstream prevention | Real institutional data or connectors |

## 4. Differentiators
1. **Break DNA**: deterministic fingerprints, similarity explanations, isolated vs recurring status.
2. **Resolution Simulator**: side-by-side "what if" estimates with documented assumptions.
3. **Root Cause to Source / Recurring Break Radar**: patterns by cause × source across cycles, with preventive actions and recurrence-after-resolution tracking.

## 5. Functional requirements (all implemented)
- Data Studio: upload CSV/Excel per source; preview; map columns; validate mandatory fields; detect invalid and duplicate rows; confirm import; sample data generation and download.
- Reconciliation: transaction ID, reference, amount, dates, account; configurable amount/date tolerances; exact and tolerance matches; amount mismatch, missing (each direction), duplicate, timing, reference mismatch, delayed feed. Runs are stored separately.
- Investigation: problem, root cause, evidence (rule IDs), similar cases, recommended and alternative action, confidence breakdown, risk; manual investigation when evidence is weak.
- Human in the loop: approve, reject (comment required), request investigation, choose an alternative action, record the final outcome. Recorded outcomes enrich the knowledge base.
- Prevention & audit: radar, root causes, source distribution, preventive recommendations, outcome history, acceptance rate, repeated-break tracking, audit log export.

## 6. Success metrics
See `../Metrics/Metrics.md`. Primary: break classification accuracy, recommendation acceptance rate, average investigation time, recurring-break frequency, false-resolution rate.

## 7. Assumptions & constraints
Synthetic data only. Single Next.js app. Supabase for cloud persistence, with browser storage as a fallback. Works without any API key. Confidence is uncalibrated.

## 8. Release criteria
The 14 acceptance criteria in `../../04_Prototype_Readme_or_Link.md` are met on the running prototype: production build passes, the automated test suite passes, and the end-to-end browser test passes on desktop and mobile.
