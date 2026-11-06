---
title: "ReconPilot — Final Report"
subtitle: "MBA ZG583 Management of AI Products · Capstone (Experiential Learning Assignment)"
---

**Team:** Team1010 · **Date:** November 2026  
**Members:** Raksha Kalegowda (2025MB26160), Nicole Maria Gomes (2025MB26037), Gurvinder Kaur (2025MB26010), Achal Tiwari (2025MB26002), Gokulkrishnan (2025MB26210), Thirumanoor Venkata Phani Bhushan (2025MB26070)

**How to read this report.** Every claim is tagged where it matters: **[Verified]** = measured or inspected in the repository; **[Assumption]** = a team assumption not yet tested with users; **[Estimate]** = an illustrative calculation; **[Future]** = planned, not built. We have conducted **no customer interviews** and collected **no user feedback**; all user statements below are hypotheses to validate in discovery.

# 1. Executive summary

**Problem.** Automated matching clears most transactions, but a long tail of reconciliation *breaks* (items that do not agree across the internal ledger, the bank statement and the payment-gateway settlement report) must still be investigated by hand. Analysts compare fields, recall rules, search past cases and chase other teams. The work is slow, depends on individual experience, and recurring root causes are rarely fixed upstream. **[Assumption — consistent with industry commentary; not measured by us.]**

**Target user.** Reconciliation analysts and operations managers in **Indian financial institutions** — banks, co-operative banks, NBFCs and payment operations teams — reconciling UPI, NEFT and IMPS collections.

**Product.** ReconPilot is an AI-assisted break **investigation and resolution** workbench. For each break it shows a structured "Break DNA" fingerprint, a probable root cause with evidence, similar historical cases, a recommended next action with a confidence score, and a simulator that compares resolution options. A human approves every decision; outcomes are recorded and retrieved for future breaks.

**Honest maturity statement.** The working prototype **[Verified]** uses **deterministic rules, hand-weighted feature similarity and nearest-case retrieval**. It uses **no trained machine-learning model and no large language model**. These components are the explainable baseline and the data-collection loop that a learned model would later have to beat.

**Recommendation: PILOT-READY PROTOTYPE → proceed to a controlled *shadow pilot*, not production.** Conditions: authentication and access control, anonymised data only, and the proof gates in §15.

# 2. Product strategy and opportunity framing

## 2.1 Product vision
*Every reconciliation break in an Indian financial institution is explained, resolved with an auditable human decision, and prevented from recurring.*

## 2.2 Jobs to be done
| Role | JTBD | Pain today [Assumption] |
|---|---|---|
| Reconciliation analyst | When a break appears in today's UPI/NEFT reconciliation, I want to see why it happened and what fixed similar breaks before, so that I can resolve it correctly before the cut-off. | Field-by-field comparison across three files; tribal knowledge; repeated research for the same patterns |
| Operations manager | When breaks pile up near month-end, I want to know which are high-risk and which keep recurring, so that I can allocate analysts and push upstream fixes. | No root-cause view across cycles; ageing discovered late |
| Risk / audit (secondary) | When I review a resolved break, I want to see the evidence and who approved what, so that I can confirm the control operated. | Decisions scattered across email and spreadsheets |

## 2.3 Opportunity framing
- **Why it matters:** India's digital payment volume (UPI in particular) multiplies the number of transactions each institution must reconcile across banks, aggregators and internal books. Each unexplained break is a potential customer complaint, financial misstatement or regulatory finding. **[Assumption — volume growth is widely reported; break rates per institution are not known to us.]**
- **Why current alternatives are weak for our wedge:** enterprise platforms (§4) are strong at matching and exception workflow but are priced and implemented for large institutions; smaller co-operative banks and NBFCs often rely on spreadsheets plus core-banking reports. **[Assumption — to validate in discovery.]**
- **Why AI may help:** investigation is a pattern-recognition and retrieval problem — "which known failure mode does this break resemble, and what worked last time?" That is where similarity search and, later, learned classifiers add value over fixed matching rules.

## 2.4 AI opportunity matrix
| Idea | Business value | Feasibility now | Priority |
|---|---|---|---|
| Root-cause suggestion for breaks | High — biggest share of analyst time [Assumption] | High — rules + similarity work on synthetic data [Verified] | **1 (MVP)** |
| Similar-case retrieval with outcomes | High — captures tribal knowledge | High | **1 (MVP)** |
| Resolution simulator | Medium — supports decisions | Medium — heuristic only | 2 |
| Recurring-break radar / prevention | High for managers | High (counting) | 2 |
| Auto-matching improvement (ML) | Medium — incumbents already strong | Low — needs real data | 3 |
| Autonomous resolution / posting | High but risky | Low — governance not ready | **Rejected for now** |

## 2.5 Build vs buy vs partner
- **Recommended path: Build the investigation layer; partner for matching and data connectors.** ReconPilot should sit *on top of* an institution's existing matching engine (or a partner's), consuming its breaks.
- **Why:** matching is a crowded, mature category; the differentiated job is investigation, explanation and prevention. Building our own thin matching engine was necessary only to make the prototype self-contained.
- **Trade-offs:** dependence on partners' data formats; we must prove value on top of matching that is already good. A future learned model could use an LLM API for narrative explanations (**[Future]**, buy/API) but root-cause decisions should stay in auditable, testable components.

## 2.6 First wedge
UPI, NEFT and IMPS **collection** reconciliation for a mid-size NBFC or co-operative bank: internal ledger vs collection-account bank statement vs payment-aggregator settlement report. This is the scenario the Indian Banking dataset demonstrates **[Verified]**.

## 2.7 Course case lens
- **iMerit (data operations and labelling quality):** our evaluation is only as good as our ground truth. Lesson transferred: labels must be produced independently of the system being evaluated — we hand-wrote the Indian answer key in a module that never imports the engines, enforced by a test **[Verified]**. What we would do differently: have a second person label pilot breaks blind.
- **Bias in Lending / Apple Card (governance):** opaque automated decisions erode trust even when accurate. Lesson: every recommendation in ReconPilot shows its rule IDs and evidence, and no decision executes without a named human.

# 3. Competitor comparison

| | Duco | SmartStream (TLM Reconciliations Premium, Air) | Fractal (Recon Assist) | ReconPilot (prototype) |
|---|---|---|---|---|
| Positioning | Cloud, no-code reconciliation and data automation platform for financial services | Enterprise reconciliation and exception management, cloud/on-prem/managed | AI solution from an analytics firm aimed at reconciliation break resolution | Investigation and resolution layer for Indian institutions |
| AI claims (vendor) | AI-based matching, label prediction for exceptions, unstructured-data ingestion; launched an agentic workspace with human-in-the-loop approval (2026) | "Affinity" observational-learning ML that learns from users' matching actions | Marketed as accelerating resolution, improving accuracy and preventing recurrence | **None implemented** — deterministic rules + hand-weighted similarity [Verified] |
| Matching engine | Mature | Mature | Not assessed | Basic (key + fuzzy), for demo only |
| India-specific UPI/NEFT/IMPS focus | Not a stated focus | Not a stated focus | Fractal is India-headquartered; product detail not assessed | Core focus |
| Target buyer | Large financial institutions | Large banks and financial institutions | Large enterprises | Mid-size banks, co-op banks, NBFCs [Assumption] |

**Honest reading.** Duco and SmartStream already claim AI-assisted exception management, and Fractal's Recon Assist uses near-identical positioning ("accelerate resolution, improve accuracy, prevent recurrence") to ours. ReconPilot is **not** differentiated by the idea of AI for breaks. Our defensible angles, still unproven, are: (1) a narrow India-first wedge — UPI/NEFT/IMPS formats, UTR/RRN identifiers, Indian file conventions — for institutions below the enterprise tier; (2) explainability by design, with every suggestion traceable to rules and cases; (3) a resolution simulator and recurring-break radar that tie investigation to prevention. If discovery shows mid-size institutions are already served by these vendors or by core-banking modules, the wedge fails. *Competitor descriptions are from vendor and trade-press materials; we have not used their products.*

# 4. PM artifact pack

## 4.1 Problem statement
Analysts in Indian banks, co-operative banks and NBFCs spend significant time investigating reconciliation breaks between ledger, bank and aggregator records because the root cause and the correct fix are not visible from the break itself, and knowledge of past fixes is not captured. **The decision being improved:** "what caused this break and what should I do about it?"

## 4.2 PRD summary (full PRD in Appendix/PRD)
- **User problem:** slow, inconsistent break investigation; recurring causes not fixed.
- **Core workflow:** ingest three sources → reconcile → for each break see Break DNA, root cause, evidence, similar cases, recommended action → simulate options → approve/reject with comment → audit log → recurring-break radar.
- **AI role (current):** rule-based classification, hand-weighted similarity retrieval, history-informed action ranking. **(Future):** learned classifier and calibrated confidence.
- **Risks:** wrong recommendation accepted; over-trust in confidence numbers; synthetic-data overfitting; data exposure.
- **Fallback logic:** confidence < 55 → the recommended action becomes INVESTIGATE (rule R23); the analyst can still choose another action; history may override a rule action only with ≥3 similar cases, ≥60% similarity and a +15-point success margin (R24); no autonomous approval (R25).
- **Data assumptions:** three per-transaction sources with shared identifiers (transaction ID and/or UTR/RRN); dates and amounts parseable; currency present.

## 4.3 MVP hypothesis
*If analysts see the probable root cause, its evidence and similar past outcomes for each break, they will resolve breaks faster with no increase in false resolutions.* The prototype proves the workflow and logic are feasible on synthetic data; it does **not** prove the time saving.

## 4.4 Feature prioritisation
Scores 1–5 (team judgement **[Assumption]**). Priority = User value × Confidence ÷ Effort.

| Feature | User value | Effort | Confidence | Priority score | Status |
|---|---|---|---|---|---|
| Break investigation (root cause + evidence) | 5 | 3 | 4 | 6.7 | Built |
| Similar historical cases | 4 | 2 | 4 | 8.0 | Built |
| Human approve/reject + audit log | 5 | 2 | 5 | 12.5 | Built |
| CSV/Excel ingest with mapping & validation | 4 | 2 | 5 | 10.0 | Built |
| Recurring Break Radar | 4 | 2 | 3 | 6.0 | Built |
| Resolution Simulator | 3 | 3 | 2 | 2.0 | Built (heuristic) |
| Authentication & roles | 5 | 2 | 5 | 12.5 | **Not built — pilot blocker** |
| Learned root-cause model | 4 | 4 | 2 | 2.0 | Future |
| Bank/aggregator connectors | 4 | 5 | 3 | 2.4 | Future |
| Autonomous resolution | 3 | 5 | 1 | 0.6 | Rejected |

*Trade-off we made:* the simulator scored low but was built because it demonstrates decision support; authentication scored highest but was deferred because the prototype uses synthetic data only. It is now the top pilot blocker.

## 4.5 How these artifacts change because the product is AI-assisted
| Artifact | What we changed |
|---|---|
| Problem statement | Framed around a *decision* (cause + action), not a screen |
| User stories | Include "when the system is unsure" and "when the system is wrong" paths |
| PRD | Data assumptions, fallback rules (R23–R25), and evaluation against independent ground truth |
| Roadmap | Proof gates with numeric thresholds before each phase |
| Metrics | Technical accuracy linked to business metrics (time, false resolution) and trust metrics (override rate) |
| Pricing | Includes operating and human-review costs |

# 5. UX, workflow and trust design

## 5.1 Main workflow (five screens, all built [Verified])
1. **Command Centre** — breaks, exposure, high-risk items, quick start.
2. **Data & Reconciliation Studio** — choose the Nexora Global or Indian Banking sample, or upload CSV/Excel; map columns; see row-level validation errors; run reconciliation; see validation against ground truth.
3. **Investigation Workbench** — break list with filters; Break DNA; probable root cause with evidence and rule IDs; similar cases; next best action and confidence; approve/reject.
4. **Resolution Simulator** — compare actions on estimated success, time and risk.
5. **Prevention & Audit Centre** — Recurring Break Radar, preventive recommendations, audit log.

Screenshots: Appendix/Screenshots_or_Video. Screen layouts: Appendix/Wireframes.

## 5.2 Trust and explainability
- **Visible:** the evidence facts, the rule IDs that fired, the similar cases and their outcomes, the confidence score and its components, and a label that scores are heuristic.
- **Hidden:** raw weight vectors and internal similarity maths (available in docs, not on the main screen) to avoid false precision.
- **Must be clear:** that the human, not the system, decides.

## 5.3 Uncertainty handling
- **High confidence (≥ 55):** show the recommended action first, still requiring approval.
- **Low confidence (< 55):** suggest INVESTIGATE (R23) and show why confidence is low; the analyst decides.
- **Failure / fallback:** invalid rows are rejected with row-level errors rather than guessed; records in different currencies are never matched (rule R28) and appear as a currency-mismatch break.

## 5.4 Human-in-the-loop
Every decision requires a named analyst; rejection requires a comment; outcomes recorded by analysts become retrievable cases. **No automatic resolution or posting is implemented.** The audit log records actor, time and detail but is **not tamper-proof** (ordinary database rows).

# 6. AI task framing and implementation architecture

## 6.1 Problem as AI tasks
| Task | Type | Current technique [Verified] | Future technique [Future] |
|---|---|---|---|
| Break detection | Rule-based matching | Key match on transaction ID then reference; fuzzy pairing within same account, same currency, amount/date tolerance and reference similarity | Unchanged (deterministic is appropriate) |
| Break type & root cause | Multi-class classification | Hand-written rules (R09–R19, R28) | Learned classifier trained on analyst-confirmed outcomes, benchmarked against these rules |
| Similar cases | Retrieval / ranking | **Break DNA**: hand-weighted feature similarity (fixed weights) + nearest-case retrieval over historical cases | Learned similarity weights |
| Next best action | Recommendation | Rule mapping, overridden by similar-case outcomes under R24 | Contextual ranking with calibrated success probabilities |
| Confidence | Scoring | Additive evidence points, capped at 97, **uncalibrated** | Calibrated on outcomes |

## 6.2 Architecture
Next.js 16 / TypeScript web app; engines are pure TypeScript modules used both in the browser and by API routes; storage in the browser (IndexedDB) or Supabase PostgreSQL; deployed on Vercel. 28 business rules parameterise the engines. No external AI API is called.

## 6.3 About "learning" and historical agreement
New analyst outcomes are added as cases and retrieved later; **no model is retrained**. The 200 seed historical cases are synthetic and their outcomes are random-number generated. When the engine says "resolved 100% of 2 similar cases", that is retrieval over synthetic history — **it is not independent validation**, and we do not count agreement with historical cases as accuracy.

# 7. Data assumptions and ground truth

## 7.1 Datasets [Verified]
| | Nexora Global | Indian Banking |
|---|---|---|
| Institution | Fictional Nexora Financial Services | Fictional Aravalli Co-operative Bank + fictional RupeeRail aggregator |
| Currency | Multi-currency (USD default) | INR only |
| Rails | ACH/wire/card/payout-style | UPI, NEFT, IMPS |
| Size | ~3,000 records per cycle, cycles generated by seed | 139 ledger, 135 bank, 136 gateway valid rows + 6 invalid rows |
| Ground truth | Generator labels (`gt_key`, `gt_scenario`, `gt_leg`) | Hand-written answer key per scenario, in a module that never imports the engines |

Details: Appendix/Data/Datasets_and_Ground_Truth.md.

## 7.2 Indian Banking scenarios
Scenarios: (1) successful UPI; (2) UPI amount mismatch, plus a hard paise-rounding case; (3) UPI missing in bank; (4) NEFT missing in ledger; (5) duplicate UPI (webhook retry, double posting); (6) delayed settlement (lag, weekend roll); (7) incorrect reference (truncation, formatting, transposition) plus a hard bank-substituted reference; (8) gateway fee netting (MDR + GST); (9) multiple errors in one cycle (dropped batch, late statement); (10) invalid or incomplete rows.

## 7.3 Key assumptions
Per-transaction gross lines (no batched net settlement); every collection passes through the aggregator; one fixed 12-day window; no holiday calendar; names and identifiers fictional; **no real financial data is used or permitted**.

# 8. Evaluation and baseline limitations

## 8.1 Results — reported separately, synthetic only [Verified]
**Nexora Global (cycles 1–5, default tolerances):** matching accuracy 100% with 0 false matches; 195 expected breaks per cycle, 0 missed, 3–5 false breaks; break-type classification accuracy 97.4–98.5%. These results are unchanged by the Indian work (pinned by regression tests).

**Indian Banking (`npm run eval:indian`):**

| Metric | Result |
|---|---|
| Matched pairs | 260 (match precision 100%, recall 100%, false match rate 0%) |
| Breaks reported | 20 (19 expected; break detection precision 95.0%, recall 100%) |
| Break-type accuracy | 94.7% (18/19) |
| Root-cause accuracy | 89.5% (17/19) |
| Recommendation accuracy | 73.7% (14/19) |
| Invalid-record handling | 6/6 rejected on the expected field; 0 valid rows rejected |

**Automated tests:** 57 passed (21 engine, 12 regression, 24 Indian); production build succeeds [Verified on 6 Nov 2026].

## 8.2 Known failures (kept on purpose)
- **Paise rounding (hard case):** labelled "FX conversion rounding" with confidence 90, because rule R10 treats any small difference on a non-USD amount as FX rounding — wrong for a domestic INR posting.
- **Bank-substituted reference (hard case):** cannot be paired; shown as "missing in bank" plus one false "missing in ledger".
- **Recommendation misses (5 of 19; 14/19 = 73.7% correct):** (1) the paise-rounding hard case above — wrong root cause, so CORRECT_REF is suggested instead of INVESTIGATE (IN-0122); (2–3) history overrides drawn from synthetic seed outcomes change the action to INVESTIGATE (R24; IN-0125 webhook duplicate, IN-0136 batch drop); (4–5) confidence 48 is below the R23 threshold, so the engine suggests INVESTIGATE (IN-0134, IN-0135 batch drop) — the intended conservative behaviour, but scored as misses.

## 8.3 Why these numbers are not real-world accuracy
The scenarios were written by people who know the rule set, so this is **not a blind test**; scores show the engine behaves as designed. Synthetic data lacks the messiness of real bank files. Confidence is uncalibrated. Nexora history is USD-oriented. **No baseline has been measured against a current manual process**; the planned pilot baseline is the institution's own historical investigation time and false-resolution rate, plus a simple "break type → default action" rule table as a technical baseline.

## 8.4 Evaluation framework
| Type | Metric | Why |
|---|---|---|
| Technical | Root-cause accuracy vs analyst-confirmed cause; break detection precision/recall | Core correctness |
| Business | Median investigation time per break; breaks cleared before cut-off | The value hypothesis |
| Trust / guardrail | False-resolution rate; override rate; % of low-confidence breaks where the INVESTIGATE suggestion was appropriate | Safety and calibration of trust |

## 8.5 Go/no-go thresholds for pilot exit [Assumption]
Root-cause accuracy ≥ 80% on analyst-confirmed pilot breaks; median investigation time −20% vs baseline; false-resolution rate not worse than baseline; zero security incidents.

# 9. Business model, monetisation and unit economics

## 9.1 Monetisation [Assumption]
Annual SaaS subscription tiered by monthly break volume, with an implementation fee for data mapping; on-premise/private-cloud option likely required by banks. No price has been tested with buyers.

## 9.2 Value logic
Value = analyst hours freed by faster investigation + avoided losses from wrong or late resolutions + reduced recurrence after upstream fixes. Only the first is modelled below; freed hours are **capacity**, not cash, unless redeployed.

## 9.3 Cost drivers
Hosting and database; support and rule maintenance (the main cost, because rules need domain upkeep); implementation/data mapping; human review time (unchanged — humans approve every break); **model/API cost currently ₹0** (no external AI). A future LLM explanation feature would add per-break inference cost.

## 9.4 Illustrative ROI scenarios [Estimate — every input marked * is an assumption]
| Scenario | Breaks/month* | Min per break* | Analyst ₹/hr* | Manual cost/month | Time saved* | Value of time saved | Platform operating cost* | Net operational saving/month | Break-even time saving |
|---|---|---|---|---|---|---|---|---|---|
| A · Co-operative bank (small) | 2,000 | 20 | 500 | ₹3,33,333 | 20% | ₹66,667 | ₹45,000 | ₹21,667 | 13.5% |
| B · NBFC / mid-size bank | 10,000 | 20 | 650 | ₹21,66,667 | 25% | ₹5,41,667 | ₹1,00,000 | ₹4,41,667 | 4.6% |
| C · Payments ops (large) | 40,000 | 15 | 800 | ₹80,00,000 | 30% | ₹24,00,000 | ₹2,40,000 | ₹21,60,000 | 3.0% |

Platform operating cost = hosting (₹15k / ₹40k / ₹1.2L) + support and rule upkeep (0.25 / 0.5 / 1 FTE at ₹1.2L per month). Excludes subscription margin, implementation fees and sales cost. **These are not customer savings.** Insight: the small co-operative bank case is marginal, which supports targeting mid-size institutions first.

## 9.5 Scaling risks
Rule maintenance grows with each new institution's formats; one-to-many batch settlement is not supported; browser-side engine is fine at ~3k records (~0.1 s) but large volumes need server-side jobs; governance burden (bank IT/security reviews) lengthens sales cycles.

# 10. Ethics, privacy, governance, risk and launch blockers

## 10.1 Main risks
1. **Wrong recommendation accepted** → financial misstatement or customer harm (e.g., a genuine duplicate debit left unrefunded).
2. **Over-trust** in confidence numbers that are uncalibrated.
3. **Data exposure** — the deployed cloud app has **no authentication**.
4. **Biased learning** — outcomes from a few analysts or synthetic history steering recommendations (R24).
5. **Currency-agnostic risk thresholds** (R20: 5,000 / 50,000 / 2,50,000) rate INR amounts as riskier than equivalent USD amounts — mis-prioritisation.
6. **Unsafe output** — no generative text exists today; if LLM explanations are added, hallucinated evidence becomes a risk.

## 10.2 Harm scenarios
A customer's failed-but-debited UPI payment is classified as a timing difference and left to "hold", delaying the refund; an auditor relies on an audit log that could be edited by a database administrator.

## 10.3 Controls [Verified unless marked]
Human approval for every decision (R25); low-confidence guardrail (R23); conservative history-override thresholds (R24); currency guard (R28); row-level validation; service-role key kept server-side and Supabase row-level security enabled with no anonymous policies; audit log of imports, runs and decisions. **[Future]:** authentication and roles, four-eyes approval above thresholds, immutable audit storage, per-currency thresholds, calibration.

## 10.4 Launch blockers (pilot cannot start until resolved)
- **No authentication / access control.** Use of real financial or customer data in the current app is **prohibited**.
- No data-processing agreement, data-residency review or information-security assessment with a pilot institution.
- Currency-specific risk thresholds and domestic-rounding rule not fixed.
- Audit log not tamper-evident.
- Spreadsheet library security advisory (SheetJS 0.18.5) not resolved.

# 11. Roadmap with proof gates
| Phase | Scope | Proof gate to exit |
|---|---|---|
| **0 · Now (done)** | Prototype, two synthetic datasets, independent answer key, 57 tests | Gate met: workflow demonstrable; Indian synthetic scores reported with limits |
| **1 · Discovery (4–6 weeks)** [Future] | 8–10 interviews with analysts/managers at co-op banks and NBFCs; collect anonymised break samples | ≥ 6 of 10 confirm investigation (not matching) is the main time sink; ≥ 2 institutions agree to a shadow pilot |
| **2 · Pilot readiness (6–8 weeks)** [Future] | Auth & roles, four-eyes, per-currency thresholds, domestic-rounding rule, tamper-evident audit, SheetJS upgrade, security review | All launch blockers closed; pen-test with no high findings |
| **3 · Shadow pilot (8–12 weeks)** [Future] | ReconPilot runs alongside analysts on anonymised data; analysts record true causes | Root-cause accuracy ≥ 80%; median investigation time −20%; false-resolution rate not worse than baseline |
| **4 · Learned models** [Future] | Train classifier on confirmed outcomes; calibrate confidence | Beats rule baseline by ≥ 5 points on held-out pilot data; calibration error within agreed limits |
| **5 · Scale** [Future] | Connectors, batch settlement, multi-institution | Positive unit economics in ≥ 2 paying customers |

# 12. Recommendation — go/no-go

**Go for a controlled shadow pilot preparation; no-go for production or real data today.** The prototype credibly demonstrates the investigation workflow, explainable logic, human-in-the-loop control and an honest evaluation method on two synthetic datasets. It does not prove time savings, real-world accuracy or market differentiation against Duco, SmartStream or Fractal. The next investment should buy evidence (discovery interviews and a shadow pilot), not features.

# Appendix references
PRD · Wireframes · Metrics · Roadmap · Risk_Note · Data (datasets and ground truth) · Competitors · Economics · Screenshots — all in `Appendix/`. Repository: https://github.com/krish19098/Reconpilot.

*Sources for competitor statements: Waters Technology rankings and awards pages on Duco (2024, 2025) and SmartStream (2021–2022); Nordic Capital case study on Duco (2026); fractal.ai Recon Assist page. Accessed 6 Nov 2026.*
