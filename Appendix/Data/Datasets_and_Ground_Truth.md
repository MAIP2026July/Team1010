# Datasets and ground truth

Both datasets are synthetic. **No real customer, account or transaction data is used, and none may be uploaded to the current app (no authentication).**

## Nexora Global (original)
- Fictional Nexora Financial Services; multi-currency (blank currency defaults to USD).
- Deterministic generator (`src/lib/engine/generator.ts`), ~3,000 records per two-week cycle across ledger, bank and gateway, with injected break scenarios.
- Ground truth: generator labels on every row — `gt_key` (one business transaction), `gt_scenario`, `gt_leg`. Includes a deliberately unmatchable "remapped bank reference" scenario so scores are not trivially 100%.
- 200 synthetic historical cases with random-number-generated outcomes (used for similar-case retrieval; **not** evidence of accuracy).

## Indian Banking (added Nov 2026)
- Fictional **Aravalli Co-operative Bank** collecting for business customers via the fictional aggregator **RupeeRail**; INR only; UPI, NEFT, IMPS; 5–16 Oct 2026.
- Files: `indian_banking_internal_ledger.csv`, `indian_banking_bank_statement.csv`, `indian_banking_payment_gateway.csv` (also Excel via the Studio), plus `indian_banking_expected_results.csv` (answer key).
- Indian conventions: UTR/RRN references, `UTR No` / `rrn` / `payment_id` column names, DD/MM/YYYY bank dates, Indian digit grouping (7,18,328.74).
- Size: 139 ledger, 135 bank, 136 gateway valid rows; 6 invalid rows.

| # | Scenario | Expected outcome (hand-written) |
|---|---|---|
| 1 | Successful UPI | Matched on both legs |
| 2 | UPI amount mismatch (keying 12,345 → 12,435); hard case paise rounding 1,250.00 vs 1,249.60 | Amount mismatch · keying error · escalate; hard case: unexplained amount · investigate |
| 3 | UPI missing in bank | Missing in bank · not captured · investigate |
| 4 | NEFT missing in ledger | Missing in ledger · unrecorded receipt · investigate |
| 5 | Duplicate UPI (webhook retry; ledger double posting) | Duplicate · escalate |
| 6 | Delayed settlement (+2 days; weekend roll) | Timing difference · hold |
| 7 | Incorrect reference (truncation, formatting, transposition); hard case bank-substituted reference | Reference mismatch · correct reference; hard case: mapping mismatch · investigate |
| 8 | Gateway fee netting (MDR 1.8% + 18% GST) | Amount mismatch · fee netting · escalate |
| 9 | Multiple errors: dropped gateway batch (3); late last-day statement (3) | Batch drop · escalate; late file · retry |
| 10 | Invalid rows: blank amount, month 13, 31/02, currency "RS", blank account, no identifier | Rejected by validation on the named field |

## How the ground truth stays independent
1. Expected type, root cause and action were written by hand per scenario in `src/lib/engine/indian-banking.ts`.
2. That module imports only types, the ingest parser and utilities — never the reconciliation or investigation engines (a unit test asserts its import list).
3. Evaluation compares engine output to this key; engine predictions are never written back as labels.
4. Agreement with the 200 synthetic historical cases is **not** counted as validation (circular).

## Limits
Not blind (authors knew the rules); per-transaction gross lines only (no batched net settlement); one fixed window; no holiday calendar; risk thresholds are currency-agnostic; historical cases are Nexora/USD.
