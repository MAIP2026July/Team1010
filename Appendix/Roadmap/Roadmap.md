# Roadmap

## Now: MVP (delivered)
- Synthetic Nexora data with ground truth; CSV/Excel ingestion with mapping and validation
- Deterministic three-way reconciliation; Break DNA; explainable investigation engine
- Resolution Simulator; Recurring Break Radar; human approval with audit; case-based learning
- Local demo mode and Supabase cloud mode; Vercel-ready

## Next: pilot readiness
- Authentication (Supabase Auth), roles (analyst / supervisor), per-user RLS policies
- Four-eyes approval above value thresholds; SLA ageing alerts
- Editable business rules UI with versioning; rule-change audit
- Live Supabase + Vercel deployment and verification; performance testing at 50–100k records
- Upgrade SheetJS to ≥ 0.20.2; server-side file validation

## Later: intelligence and integration
- Optional LLM narrative explanations over the structured investigation (Claude/OpenAI), clearly labelled
- Calibrate confidence on real outcome data (reliability curves) before showing probabilities
- Learned similarity weights and root-cause classifier trained on recorded decisions, with model-risk governance
- Connectors (bank MT940/camt.053, gateway settlement reports, ERP/GL); scheduled runs
- Prevention workflow: create and track upstream tickets, then measure recurrence before and after the fix

## Proof gates (added for the final submission)
| Phase | Exit gate |
|---|---|
| Discovery (4–6 wks) | ≥ 6 of 10 interviewed analysts/managers confirm investigation is the main time sink; ≥ 2 institutions agree to a shadow pilot |
| Pilot readiness (6–8 wks) | Authentication + roles, four-eyes, per-currency risk thresholds (R20), domestic-rounding rule (R10), tamper-evident audit, SheetJS upgrade; security review with no high findings |
| Shadow pilot (8–12 wks) | Root-cause accuracy ≥ 80% on analyst-confirmed breaks; median investigation time −20% vs baseline; false-resolution rate not worse than baseline |
| Learned models | Classifier beats the rule baseline by ≥ 5 points on held-out pilot data; confidence calibrated |
| Scale | ≥ 2 paying customers with positive unit economics |

All phases after "Now" are future plans; thresholds are team assumptions.
