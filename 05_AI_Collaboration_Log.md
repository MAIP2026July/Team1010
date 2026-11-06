# 05 · AI Collaboration Log: ReconPilot

**Team:** Team1010 · Members: Raksha Kalegowda (2025MB26160), Nicole Maria Gomes (2025MB26037), Gurvinder Kaur (2025MB26010), Achal Tiwari (2025MB26002), Gokulkrishnan (2025MB26210), Thirumanoor Venkata Phani Bhushan (2025MB26070)

Sections follow the mandatory template in the Capstone Student Packet (§7.9). AI use is documented only where evidence exists (the build, audit and submission sessions directed by Gokulkrishnan). Other members' individual AI use was not separately logged and requires member confirmation; no member's AI use has been invented.

## Tools used
| Tool | Used for | By |
|---|---|---|
| Claude Code (Anthropic, cloud session working in the GitHub repo) | Prototype design and coding, tests, compliance audit, Indian Banking dataset, documentation drafts, PDF/deck generation | Gokulkrishnan (2025MB26210) |
| Claude (chat) | Explanations of the build, differentiation brainstorming, manual drafting | Gokulkrishnan (2025MB26210) |
| ChatGPT | Not recorded in the project files; individual usage was not separately logged and requires member confirmation | Not confirmed |
| Individual usage not separately logged; requires member confirmation | Team-level activity; individual allocation was not separately recorded | Raksha Kalegowda (2025MB26160) |
| Individual usage not separately logged; requires member confirmation | Team-level activity; individual allocation was not separately recorded | Nicole Maria Gomes (2025MB26037) |
| Individual usage not separately logged; requires member confirmation | Team-level activity; individual allocation was not separately recorded | Gurvinder Kaur (2025MB26010) |
| Individual usage not separately logged; requires member confirmation | Team-level activity; individual allocation was not separately recorded | Achal Tiwari (2025MB26002) |
| Individual usage not separately logged; requires member confirmation | Team-level activity; individual allocation was not separately recorded | Thirumanoor Venkata Phani Bhushan (2025MB26070) |

## Where AI helped
- **Discovery / framing:** brainstorming differentiators versus existing reconciliation products; restating the problem around the investigation *decision*.
- **Drafting:** PRD structure, README, metrics definitions, risk note, final report and executive summary first drafts.
- **Wireframing:** text wireframes of the five screens.
- **Coding:** the full Next.js prototype (engines, five screens, ingest, persistence, API), the Indian Banking dataset and its evaluation script.
- **Metrics:** ground-truth evaluation design (separate match, break, root-cause and recommendation metrics) and the scenario ROI calculation (run in code, not estimated in prose).
- **Risk review:** a capstone compliance audit of the repository against the packet, which surfaced the missing deliverables, the no-auth blocker and overstated AI claims.

## Example prompts and workflows (actual)
- **Prompt 1 — audit (paraphrased from the user's message):** "Audit the existing implementation, screens, APIs, database schema, tests and documentation against the student packet. Do not modify any code. Do not create new files. Do not assume a feature exists just because it is mentioned in the PRD or README." → Output: gap list and risk findings, later saved as a Claude Doc.
- **Prompt 2 — Indian Banking dataset (key rules quoted from the brief):** "Preserve the existing Nexora dataset. Preserve existing reconciliation functionality… Add regression tests for existing functionality. Add tests for all new Indian scenarios… If any existing engine behaviour needs modification, explain the reason and scope before making the change." → Workflow: AI proposed three engine changes (currency guard R28, Indian ingest formats, a new break type); the user approved them; AI built them on a branch and opened PR #2.
- **Prompt 3 — finalisation sprint:** "Complete all mandatory academic deliverables with accurate, consistent and defensible content… Do not claim trained ML or Generative AI exists… Do not fabricate customer interviews, market research, ROI, revenue, user feedback or team contributions." → Output: 01–06, appendix additions, illustrative ROI model.
- Other members' prompts: individual usage was not separately logged and requires member confirmation.

## Where AI was weak or wrong
| Issue | Detail |
|---|---|
| USD-centric rules | Rule R10 (written with AI help) treats any small non-USD variance as FX rounding; on Indian data it mislabels domestic paise rounding with confidence 90. The rule-writing did not anticipate a single-currency domestic market. |
| Currency-agnostic risk thresholds | R20 thresholds were set in one currency; INR amounts are rated riskier than equivalent USD amounts. Not fixed (documented). |
| Non-blind test design | AI wrote the Indian scenarios while knowing the rules, so high scores are partly by construction. Hard cases had to be added deliberately to expose limits. |
| Synthetic history presented persuasively | The engine's rationale says e.g. "100% success across 5 similar cases" — these outcomes are random-number generated. Such text could be mistaken for evidence. |
| Missed competitor overlap | Early differentiation ideas did not surface that Fractal's Recon Assist uses near-identical positioning ("accelerate resolution, improve accuracy, prevent recurrence"); found only by a web check during the final sprint. |
| Stale documentation | Rule counts (27 vs 28) and test counts went out of date across docs after changes; caught by a search before submission. |
| Engineering misses found by verification | Amount parser accepted "abc" as 0; mobile tables overflowed; cloud payload could exceed Vercel's 4.5 MB limit; a Markdown table broke on `|` in IDs. All fixed after tests or screenshots exposed them. |
| Other members' observations | Not separately logged; requires member confirmation |

## Human corrections and validation
| What we changed | Why | Judgement applied |
|---|---|---|
| Rejected LLM/ML claims; described engines as deterministic rules + hand-weighted similarity | Claims must match the code | Honesty over hype; the packet penalises unsupported "AI" claims |
| Required approval before any engine change | Protect Nexora behaviour and existing results | Change control; regression tests pin Nexora cycles 1–5 |
| Kept the Indian answer key in a module that cannot import the engines | Avoid circular evaluation | Ground truth must be independent of predictions |
| Kept known failures in reported metrics | Avoid inflated scores | Transparency for graders and future pilot partners |
| Did **not** merge PR #2 during the final sprint | Merging to `main` auto-deploys production on Vercel; the brief said not to deploy automatically | Protect the working deployment; merge is a human decision |
| Labelled every ROI input as an assumption and kept freed hours as "capacity, not cash" | No customer data exists | Avoid fabricated business impact |
| Kept "PILOT preparation, not production" recommendation | No auth, no real-data evidence | Launch discipline |
| Other members' corrections | Team-level activity; individual allocation was not separately recorded | See 06 for project-level validation |

**Validation performed:** `npx vitest run` (57 passed), `npx tsc --noEmit`, `npx eslint src`, `npm run build`, `npm run eval:indian`, browser checks of all five screens with both datasets, and a search of all docs for stale numbers. Team members must still review domain logic (root-cause rules, action mapping, simulator assumptions) — These validation activities were conducted as part of the team project. Individual responsibility for each activity was not separately recorded..

## Final reflection
- **Where AI accelerated PM work:** turning a written concept into a working, testable prototype in days; generating consistent artifacts from one source of truth; running the ROI arithmetic and evaluation in code; auditing claims against the repository.
- **Where AI could not replace PM reasoning:** choosing the India-first wedge and target segment; deciding what not to build (autonomous resolution); accepting or rejecting risk (no real data without auth); interpreting that the small co-op bank ROI scenario is marginal; deciding the go/no-go; and spotting that a confident engine rationale built on synthetic history is not evidence.
- Individual reflections were not separately recorded; members may add their own on confirmation.

---

## Member confirmation of AI use
| Member | AI tools used personally | Confirmed |
|---|---|---|
| Raksha Kalegowda (2025MB26160) | Individual usage not separately logged; requires member confirmation | Pending |
| Nicole Maria Gomes (2025MB26037) | Individual usage not separately logged; requires member confirmation | Pending |
| Gurvinder Kaur (2025MB26010) | Individual usage not separately logged; requires member confirmation | Pending |
| Achal Tiwari (2025MB26002) | Individual usage not separately logged; requires member confirmation | Pending |
| Thirumanoor Venkata Phani Bhushan (2025MB26070) | Individual usage not separately logged; requires member confirmation | Pending |
| Gokulkrishnan (2025MB26210) | Claude Code, Claude chat (documented above) | Verified from session records |

## Appendix A — Build session details (6 Nov 2026)
| Area | Output |
|---|---|
| Architecture | Next.js 16 / TypeScript / Tailwind; pure engine modules shared by browser and API routes; IndexedDB or Supabase repository |
| Data | Seeded Nexora generator with ground truth; 200 synthetic historical cases; 28 business rules (R28 added with the Indian dataset); Indian Banking dataset with hand-written answer key |
| UI | Command Centre, Studio (with dataset toggle), Investigation Workbench, Simulator, Prevention & Audit Centre |
| Quality | 57 automated tests; opt-in PostgreSQL integration test; Playwright end-to-end checks |

## Appendix B — Team entry template
| Date | Member | Tool | Purpose / prompt summary | What was used | What was changed or rejected | How it was verified |
|---|---|---|---|---|---|---|
| | | | | | | |
