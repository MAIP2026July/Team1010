---
title: "ReconPilot — Executive Summary"
subtitle: "AI-assisted reconciliation break investigation and resolution for Indian financial institutions"
---

**Team:** Team1010 · MBA ZG583 Management of AI Products · November 2026  
**Members:** Raksha Kalegowda (2025MB26160), Nicole Maria Gomes (2025MB26037), Gurvinder Kaur (2025MB26010), Achal Tiwari (2025MB26002), Gokulkrishnan (2025MB26210), Thirumanoor Venkata Phani Bhushan (2025MB26070)

## Problem
Automated matching clears most transactions, but the remaining reconciliation **breaks** — items that disagree between the internal ledger, the bank statement and the payment-gateway settlement report — are investigated by hand. Analysts compare fields across three files, recall rules, search past cases and chase other teams. The work is slow and depends on individual experience, and recurring causes are rarely fixed upstream. With UPI, NEFT and IMPS volumes rising, every unexplained break is a potential customer complaint, misstatement or audit finding. *(Problem framing is a team assumption; we have not yet run customer interviews.)*

## Target user / customer
- **Users:** reconciliation analysts and operations managers.
- **Customers (initial wedge):** Indian banks, co-operative banks, NBFCs and payment operations teams reconciling UPI, NEFT and IMPS collections — with a first focus on mid-size institutions below the enterprise tier served by Duco and SmartStream.

## Product concept
ReconPilot is an investigation and resolution workbench that sits after matching. For each break it shows:

- **Break DNA** — a structured fingerprint of the break (type, amount and date gaps, reference similarity, source pattern);
- a **probable root cause** with the evidence and rule IDs behind it;
- **similar historical cases** and how they were resolved;
- a **recommended next action** with a confidence score, and a **Resolution Simulator** to compare options;
- a **Recurring Break Radar** that turns repeated causes into prevention work.

A named analyst approves or rejects every decision; decisions are logged and recorded outcomes become retrievable cases.

**Prototype (working web app on Vercel; the Indian dataset is on the PR #2 preview build until merged):** five screens, CSV/Excel upload with mapping and validation, and two synthetic sample datasets — *Nexora Global* (multi-currency) and *Indian Banking* (fictional co-operative bank, INR, UPI/NEFT/IMPS, 10 scenarios with an independent hand-written answer key).

## Why AI?
Matching is well served by rules. **Investigation** is different: it is pattern recognition and recall — "which known failure does this break resemble, and what fixed it last time?" — exactly where similarity retrieval and, later, learned classifiers outperform static rule lists and dashboards, while keeping a human in control.

**What is implemented today (honest maturity):** deterministic rules (28), *hand-weighted* feature similarity and nearest-case retrieval, and an uncalibrated additive confidence score. **No trained ML model and no LLM are used.** This is a deliberate explainable baseline that also collects the analyst-confirmed outcomes a future learned model would be trained and judged on.

**Evidence so far (synthetic data only, not real-world accuracy):** on the Indian dataset — 260 matched pairs, 20 breaks reported (19 expected, none missed), break-type accuracy 94.7%, root-cause accuracy 89.5%, recommendation accuracy 73.7%, 6/6 invalid rows rejected. Known failures are kept visible (domestic paise rounding mislabelled as FX rounding; a bank-substituted reference). 57 automated tests pass. The scenarios were written by the team, so this is not a blind test.

## Recommendation — **PILOT (preparation), not production**
Proceed to discovery and a **shadow pilot** on anonymised data with one or two mid-size institutions. Before any pilot: add authentication and roles (the current cloud app has none — **real financial data is prohibited**), per-currency risk thresholds, a domestic-rounding rule and a tamper-evident audit log. Exit the pilot only if root-cause accuracy reaches ≥ 80% on analyst-confirmed breaks, median investigation time falls ≥ 20%, and false resolutions do not increase. Key risk: Duco, SmartStream and Fractal already market AI-assisted exception handling; our India-first, explainable wedge must be validated with buyers.
