# Risk note

| Risk | Impact | Mitigation in MVP | Further mitigation |
|---|---|---|---|
| Wrong recommendation accepted (false resolution) | Financial misstatement | No autonomous approval (R25); evidence and rule IDs shown; below confidence 55 the suggested action becomes INVESTIGATE (R23); the analyst still decides; false-resolution rate tracked | Four-eyes above thresholds; post-resolution re-check |
| Over-trust in "AI" or confidence numbers | Poor decisions | UI and docs state the scores are heuristic and uncalibrated; simulator labelled as estimates | Calibrate on real outcomes before presenting probabilities |
| Synthetic-data bias | Overstated accuracy | Hard unmatchable cases injected; caveat published with the metrics | Validate on anonymised real data in a pilot |
| Learning from bad labels | Degraded recommendations | Only explicitly recorded outcomes enter the knowledge base; history overrides need ≥3 similar cases and a +15-point success margin (R24) | Supervisor review of analyst cases; decay old cases |
| Unauthorised access / data exposure | Confidentiality breach | Service-role key server-only; RLS enabled with no anon policies; reset disabled by default; no secrets committed | Add authentication, per-user RLS, Vercel deployment protection |
| Malicious spreadsheet upload | Client-side compromise | 10 MB limit; parsing only in the uploader's browser; advisory documented for xlsx 0.18.5 | Upgrade SheetJS; server-side sandboxed parsing |
| Regulatory / audit requirements | Non-compliance | Every import, run, re-investigation and decision is audited with actor, time and detail; CSV export | Immutable audit storage; retention policies |
| Operational scale | Slow UI or response limits | Engines ~0.1 s per 3k records; paged DB reads; cloud loads latest 4 runs | Server-side pagination; background jobs |

## Additional risks and launch blockers (final submission)
| Risk | Status |
|---|---|
| **No authentication in the deployed cloud app** | **Launch blocker.** Real financial or customer data is prohibited until auth, roles and per-user RLS exist |
| Audit log is ordinary database rows | Not tamper-proof; tamper-evident storage required before pilot |
| Currency-agnostic risk thresholds (R20: 5,000 / 50,000 / 2,50,000) | INR amounts rated riskier than equivalent USD; per-currency thresholds required |
| R10 treats small non-USD variances as FX rounding | Mislabels domestic paise rounding (hard case IN-0122, confidence 90) |
| History overrides from synthetic seed outcomes (R24) | Can steer actions without real evidence; seed history must be replaced by institution data |
| Unpaired bank-substituted references | Produce a false "missing in ledger"; reference-mapping tables needed |
| No automatic resolution | By design; any future automation needs four-eyes and rollback |
| No external AI today | No hallucination risk now; becomes a risk if LLM explanations are added (must cite structured evidence only) |
