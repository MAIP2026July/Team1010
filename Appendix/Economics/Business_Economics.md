# Business economics (illustrative)

**Status:** every input marked * is an assumption chosen by the team for illustration. No customer, price or savings figure has been measured. Freed analyst hours are capacity, not cash, unless redeployed. Reproduce with `python3 roi_model.py`.

## Monetisation [Assumption]
Annual SaaS subscription tiered by monthly break volume + one-time implementation fee (data mapping, rule tuning). Private-cloud/on-premise option likely needed for banks. Price not tested with buyers.

## Cost drivers
| Driver | Today | At pilot/scale |
|---|---|---|
| Model / API | ₹0 — no external AI is called | Per-break inference cost if LLM explanations are added [Future] |
| Hosting & database | Vercel + Supabase free/low tiers | Scales with data volume and private-cloud needs |
| Support & rule upkeep | Team time | Largest cost: domain experts maintain rules per institution |
| Implementation | — | Mapping each institution's files, connectors |
| Human review | Every break approved by an analyst | Unchanged by design (no autonomous resolution) |

## Scenario ROI model
| Scenario | Breaks/month* | Min per break* | Analyst ₹/hr* | Manual hours/month | Manual cost/month | Time saved* | Hours saved | Value of time saved | Hosting* | Support & rule upkeep* | Platform operating cost | Net operational saving/month | Break-even time saving |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A · Co-operative bank (small) | 2,000 | 20 | 500 | 667 | ₹333,333 | 20% | 133 | ₹66,667 | ₹15,000 | ₹30,000 | ₹45,000 | ₹21,667 | 13.5% |
| B · NBFC / mid-size bank | 10,000 | 20 | 650 | 3,333 | ₹2,166,667 | 25% | 833 | ₹541,667 | ₹40,000 | ₹60,000 | ₹100,000 | ₹441,667 | 4.6% |
| C · Payments ops (large) | 40,000 | 15 | 800 | 10,000 | ₹8,000,000 | 30% | 3,000 | ₹2,400,000 | ₹120,000 | ₹120,000 | ₹240,000 | ₹2,160,000 | 3.0% |

**Formulae.** Manual hours = breaks × minutes ÷ 60. Manual cost = hours × analyst ₹/hr. Value of time saved = manual cost × time-saved %. Platform operating cost = hosting* + support FTE* × ₹1,20,000*/month. Net operational saving = value of time saved − platform operating cost. Break-even time saving = platform operating cost ÷ manual cost.

**Reading.** Scenario A (small co-op bank) is marginal; B and C break even at under 5% time saving. This supports a mid-size-first wedge — *if* the time-saving hypothesis survives the shadow pilot. The 20–30% time-saved inputs are hypotheses; the pilot exit gate is −20% median investigation time.

## Unit economics view
Gross margin depends mainly on rule-maintenance effort per customer. Standardising Indian formats (UTR/RRN, UPI/NEFT/IMPS files) across customers is what makes the model scale; bespoke per-bank rules would not.

## Scaling risks
Latency at high volume (engine runs in the browser today; ~0.1 s per 3k records); rule-maintenance cost growth; one-to-many batch settlements unsupported; long bank security and procurement cycles.
