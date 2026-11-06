# Metrics: definitions and measured results

## Product metrics (computed live in the app)
| Metric | Definition | Where |
|---|---|---|
| Match rate | records in no break ÷ all records across sources | Command Centre |
| Break rate | breaks ÷ ledger records | Command Centre |
| High-risk breaks | breaks with risk HIGH or CRITICAL (rules R20–R22) | Command Centre |
| Matching accuracy | linked pairs whose ground-truth keys agree ÷ linked pairs | Studio (synthetic data) |
| Break classification accuracy | detected true breaks with the correct type ÷ detected true breaks | Studio |
| False breaks / missed breaks | flagged but truth says matched / truth says break but matched | Studio |
| Recommendation acceptance rate | approvals using the recommended action ÷ all decisions | Command Centre, Prevention |
| Override rate | approvals with a different action ÷ all decisions | Prevention |
| Average investigation time | seconds from opening a break to recording a decision | Command Centre, Prevention |
| Recurring break frequency | breaks per pattern per cycle; pattern status chronic/recurring/isolated | Prevention (Radar) |
| False-resolution rate | approved breaks whose transaction breaks again in a later run on new data ÷ approved breaks checked | Prevention |

## Measured engine validation (synthetic Nexora data, default tolerances)
| Cycle | Linked pairs | False matches | Matching acc. | Expected breaks | Detected | False breaks | Missed | Classification acc. |
|---|---|---|---|---|---|---|---|---|
| 1 | 1945 | 0 | 100.00% | 195 | 200 | 5 | 0 | 97.4% |
| 2 | 1946 | 0 | 100.00% | 195 | 199 | 4 | 0 | 97.9% |
| 3 | 1945 | 0 | 100.00% | 195 | 200 | 5 | 0 | 97.4% |
| 4 | 1947 | 0 | 100.00% | 195 | 198 | 3 | 0 | 98.5% |
| 5 | 1947 | 0 | 100.00% | 195 | 198 | 3 | 0 | 98.5% |

Nexora results are unchanged by the Indian Banking work (pinned by `tests/regression.test.ts`). All errors come from the deliberately unmatchable "remapped bank reference" scenario: truth is reference mismatch, the engine reports missing in bank, and the orphan bank line becomes a false "missing in ledger". Engine time for one ~3,000-record run is about 80–120 ms in Node.

**Interpretation caveat:** the synthetic patterns and the engine were designed together. These numbers show the engine is correct on the designed scenarios. They do not predict accuracy on real data. Acceptance rate and investigation time are measured only from decisions recorded during demos. No business-impact figures (for example time saved) have been measured or are claimed.

## Indian Banking ground-truth evaluation (separate from Nexora)
Reproduce with `npm run eval:indian`. Fictional INR dataset (Aravalli Co-operative Bank / RupeeRail): 139 ledger, 135 bank and 136 gateway valid records, 6 invalid rows, 19 expected breaks across 10 scenarios. The expected outcome of every scenario was written by hand in `src/lib/engine/indian-banking.ts`, which does not import any engine; engine predictions are never used as ground truth.

| Metric | Result |
|---|---|
| Match precision | 100.0% (260/260) |
| Match recall | 100.0% (260/260) |
| False match rate | 0.0% |
| Break detection precision | 95.0% (19 of 20 predicted) |
| Break detection recall | 100.0% (19/19) |
| Break classification accuracy | 94.7% (18/19) |
| Root-cause accuracy | 89.5% (17/19) |
| Recommendation accuracy | 73.7% (14/19) |
| Invalid-record handling | 6/6 rejected on the expected field; 0 valid rows rejected |
| Currency-mismatch false matches | 0 (no INR record is paired with a non-INR record; guarded by R28 and regression tests) |

Errors (break classification: 1 miss, IN-0132; root cause: 2 misses, IN-0122 and IN-0132; recommendation: 5 misses, IN-0122, IN-0125, IN-0134, IN-0135, IN-0136):
- **Paise rounding (hard case, IN-0122):** expected *unexplained amount → investigate*; engine says *FX rounding → correct reference*, confidence 90. R10 assumes any small non-USD variance is FX conversion.
- **Bank-substituted reference (hard case, IN-0132):** expected *reference mismatch*; engine reports *missing in bank* plus a false *missing in ledger* orphan (the one false break).
- **Webhook-retry duplicate (IN-0125)** and **batch drop (IN-0136):** root cause correct; the action is overridden to *investigate* by similar-case history (R24). The seed history outcomes are synthetic.
- **Batch drop (IN-0134, IN-0135):** root cause correct; confidence 48 is below the R23 threshold, so the engine suggests INVESTIGATE instead of ESCALATE.

**Caveat:** the scenarios were authored by people who know the rule set, so this is not a blind test. Two hard cases were included to expose limits. These numbers do not predict accuracy on real Indian bank data.

## Proposed pilot KPIs (not yet measured)
Reduction in average break resolution time · % of breaks with an accepted recommendation · false-resolution rate · reduction in recurring breaks after upstream fixes · cost per break.
