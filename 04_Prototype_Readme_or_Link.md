# 04 · Prototype README / Links: ReconPilot

**Product:** ReconPilot, an AI-assisted reconciliation break investigation and resolution platform for Indian financial institutions
**Initial customers:** Indian banks, co-operative banks, NBFCs and payment operations teams (internal ledger vs bank statement vs payment-gateway settlement; UPI, NEFT, IMPS)
**Prototype type:** functional web application (Next.js 16 + TypeScript; browser storage or Supabase; hosted on Vercel)
**Data:** fully synthetic. Two sample datasets: **Nexora Global** (fictional Nexora Financial Services, multi-currency) and **Indian Banking** (fictional Aravalli Co-operative Bank and RupeeRail aggregator, INR).

> **Do not upload real financial or customer data.** The deployed app has no authentication.

## Links
| | |
|---|---|
| Repository | https://github.com/krish19098/Reconpilot |
| Live demo (production, `main`) | https://reconpilot-omega.vercel.app — Nexora dataset. *Set as the repository homepage; not re-checked from the final documentation session (network-restricted). Open it before submitting.* |
| Indian Banking build (PR #2 preview) | https://reconpilot-git-feature-indian-banking-dataset-reconpilot.vercel.app — Vercel reported this preview build **Ready**. Once PR #2 is merged, the production URL will include the Indian dataset. Vercel preview links may require sign-in to the Vercel team. |
| Pull request | https://github.com/krish19098/Reconpilot/pull/2 |
| Screenshots | `Appendix/Screenshots_or_Video/` (10–12 show the Indian dataset) |
| Demo video (2–3 min) | **PENDING — not recorded.** Screenshots and the walkthrough below are the current evidence. |
| Setup, architecture, API | Repository `README.md`, `docs/API.md`, `docs/DEPLOYMENT.md` |

The single official prototype is this repository and its Vercel deployment.

## What it demonstrates
The full break decision loop: ingest three sources → reconcile → investigate each break (Break DNA, probable root cause with evidence, similar cases, next best action with confidence) → compare options in the Resolution Simulator → approve or reject with a named analyst → audit log → Recurring Break Radar and preventive recommendations.

## AI role — what is actually implemented
| Capability | Technique | Trained ML? | LLM? |
|---|---|---|---|
| Matching and break detection | Deterministic rules (R01–R08, R28 currency guard) | No | No |
| Root cause | Deterministic rules (R09–R19, R28) | No | No |
| Break DNA and similar cases | Hand-weighted feature similarity + nearest-case retrieval | No | No |
| Next best action | Rule mapping; may be overridden by similar-case outcomes (R24); low-confidence fallback (R23) | No | No |
| Confidence | Additive evidence points, uncalibrated | No | No |
| "Learning" | Recorded outcomes are stored and retrieved later; nothing is retrained | No | No |

No automatic resolution or posting is implemented. Every decision needs a human.

## Run locally (2 minutes)
```bash
git clone https://github.com/krish19098/Reconpilot.git
cd Reconpilot
git checkout feature/indian-banking-dataset   # until PR #2 is merged
npm install
npm run dev     # open http://localhost:3000
```
No API keys are needed. Without Supabase variables the app runs in **local demo mode** and stores data in the browser.

## Using the datasets
**Nexora Global:** Command Centre → *Load sample data & run reconciliation*, or Data Studio → *Sample datasets* → **Nexora Global dataset** → choose cycle and count → *Load & run*.

**Indian Banking (5 minutes):**
1. Data Studio → *Sample datasets* → **Indian Banking dataset**.
2. Click **Load & run reconciliation**. Or download the three CSV/Excel files and upload them in the Ledger, Bank and Gateway cards; the six deliberately invalid rows are rejected with row-level errors.
3. Studio summary: **260** matched pairs and **20** breaks across ten scenarios (UPI amount mismatch, missing in bank, NEFT missing in ledger, duplicates, settlement delays, reference errors, gateway fee netting, a dropped batch, a late statement).
4. Download the **answer key** to compare predicted and expected outcomes. Scores: `Appendix/Metrics` (Indian section).

## Demo walkthrough (acceptance criteria → where)
| # | Step | Where |
|---|---|---|
| 1–3 | Load synthetic data or upload CSV/Excel; execute reconciliation | Command Centre quick start, or Data Studio |
| 4 | View matched and unmatched transactions | Studio › *Load matches*; Workbench |
| 5–6 | Open a break and view its Break DNA (e.g. the gateway fee-netting break) | Investigation Workbench |
| 7 | Root cause with supporting evidence and rule IDs | Workbench › *Probable root cause* |
| 8 | Similar historical cases | Workbench › *Similar historical cases* |
| 9 | Next best action and confidence | Workbench › *Next best action* |
| 10 | Compare resolutions | Resolution Simulator |
| 11 | Approve / reject (enter an analyst name first) | Workbench decision buttons |
| 12 | Decision in audit trail | Prevention & Audit Centre › Audit log |
| 13–14 | Recurring Break Radar; preventive recommendations | Prevention & Audit Centre |

## Verified results (6 Nov 2026)
- 57 automated tests pass (21 engine, 12 Nexora regression, 24 Indian); production build passes.
- Indian Banking: 260 matched pairs; 20 breaks reported (19 expected, 0 missed); break-type accuracy 94.7%; root-cause accuracy 89.5%; recommendation accuracy 73.7%; 6/6 invalid rows rejected.
- Nexora cycles 1–5: 100% matching accuracy, 0 missed breaks, 97.4–98.5% classification accuracy; unchanged by the Indian work.

## What the prototype does not prove
- Real-world accuracy: both datasets are synthetic and the team wrote the scenarios knowing the rules (not a blind test).
- Time savings or ROI: nothing has been measured with users; the economics appendix is illustrative.
- Market demand or differentiation against Duco, SmartStream and Fractal.
- Calibrated confidence: scores are heuristic.
- Production readiness: no authentication, audit log not tamper-proof, xlsx 0.18.5 advisory open.

## Known limitations
- R10 treats small non-USD variances as FX rounding, so domestic paise rounding is mislabelled (confidence 90).
- R20 risk thresholds are currency-agnostic, so INR amounts look riskier than the same value in USD.
- Bank-substituted references cannot be paired (false "missing in ledger").
- Per-transaction gross lines only; batched net settlements, holiday calendars and one-to-many matching are not supported.
- Seed history (200 cases) is synthetic Nexora/USD data with random outcomes; similar-case statistics are not evidence.
- A blank currency defaults to USD.
