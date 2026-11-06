# Team1010 · ReconPilot · MBA ZG583 Management of AI Products — Capstone submission

**Team1010:** Raksha Kalegowda (2025MB26160) · Nicole Maria Gomes (2025MB26037) · Gurvinder Kaur (2025MB26010) · Achal Tiwari (2025MB26002) · Gokulkrishnan (2025MB26210) · Thirumanoor Venkata Phani Bhushan (2025MB26070)

**Product:** ReconPilot, an AI-assisted reconciliation break investigation and resolution platform for Indian financial institutions. **Recommendation:** pilot preparation, not production.

## Files
| File | Content |
|---|---|
| `01_Executive_Summary.pdf` | Executive summary (2 pages) |
| `02_Final_Report.pdf` | Final report (9 pages): strategy, JTBD, competitors, build/buy/partner, PRD and MVP, prioritisation, UX and trust, AI framing and architecture, data and ground truth, evaluation, economics, governance, roadmap, go/no-go |
| `03_Presentation_Deck.pdf` | Presentation (12 slides) |
| `03_Presentation_Deck.pptx` | Editable presentation |
| `04_Prototype_Readme_or_Link.md` | Prototype type, links, demo walkthrough, datasets, limitations |
| `05_AI_Collaboration_Log.md` | AI collaboration log (packet §7.9 template) |
| `06_Individual_Contribution_Statement.pdf` | Individual contribution statement (PDF) |
| `06_Individual_Contribution_Disclosure.md` | Same statement, editable |
| `Appendix/PRD/ReconPilot_PRD.md` | PRD |
| `Appendix/Roadmap/Roadmap.md` | Roadmap with proof gates |
| `Appendix/Wireframes/Wireframes.md` | Screen layouts and workflow |
| `Appendix/Metrics/Metrics.md` | Metric definitions; Nexora and Indian results, reported separately |
| `Appendix/Data/Datasets_and_Ground_Truth.md` | Datasets and ground-truth method |
| `Appendix/Competitors/Competitor_Comparison.md` | Duco, SmartStream and Fractal comparison, with sources |
| `Appendix/Economics/Business_Economics.md`, `roi_model.py` | Illustrative ROI model; every input is an assumption |
| `Appendix/Risk_Note/Risk_Note.md` | Risks, controls, launch blockers |
| `Appendix/Screenshots_or_Video/` | 12 screenshots (10–12 show the Indian dataset) and an index; **demo video pending** |
| `src/` | Markdown sources and `render.sh` used to regenerate 01, 02 and 06 PDFs |

## Mapping to the ten mandatory components (packet §5)
| # | Component | Where |
|---|---|---|
| 1 | Executive Summary | `01_Executive_Summary.pdf` |
| 2 | Product Strategy and Opportunity Framing | `02_Final_Report.pdf` §2–3; `Appendix/Competitors/` |
| 3 | PM Artifact Pack | `02_Final_Report.pdf` §4 and §11; `Appendix/PRD/`, `Appendix/Roadmap/`, `Appendix/Metrics/` |
| 4 | UX / Workflow / Trust Design | `02_Final_Report.pdf` §5; `Appendix/Wireframes/`, `Appendix/Screenshots_or_Video/` |
| 5 | Data, Model, and Evaluation Strategy | `02_Final_Report.pdf` §6–8; `Appendix/Data/`, `Appendix/Metrics/` |
| 6 | Business, Economics, and Scaling View | `02_Final_Report.pdf` §9; `Appendix/Economics/` |
| 7 | Ethics, Governance, and Risk Note | `02_Final_Report.pdf` §10; `Appendix/Risk_Note/` |
| 8 | Functional Prototype / MVP | `04_Prototype_Readme_or_Link.md`, repository, live demo |
| 9 | AI Collaboration Log | `05_AI_Collaboration_Log.md` |
| 10 | Individual Contribution Disclosure | `06_Individual_Contribution_Statement.pdf` / `.md` |
| — | Presentation | `03_Presentation_Deck.pdf` / `.pptx` |

## Links
| | URL | Status |
|---|---|---|
| Repository (official prototype source) | https://github.com/krish19098/Reconpilot | The repository this project pushes to |
| Live demo (production, `main`, Nexora dataset) | https://reconpilot-omega.vercel.app | Taken from the repository homepage setting; **not opened from the documentation session** |
| Indian Banking build (PR #2 Vercel preview) | https://reconpilot-git-feature-indian-banking-dataset-reconpilot.vercel.app | Vercel reported it Ready on the PR; **not opened**; may need Vercel sign-in |
| Pull request #2 (open, not merged) | https://github.com/krish19098/Reconpilot/pull/2 | Merging deploys production |

## Facts used throughout (verified 6 Nov 2026)
57 automated tests pass; production build passes. Indian Banking: 260 matched pairs, 20 breaks (19 expected), break-type accuracy 94.7% (18/19), root-cause accuracy 89.5% (17/19), recommendation accuracy 73.7% (14/19, 5 misses), 6/6 invalid rows rejected. Nexora cycles 1–5: 100% matching, 97.4–98.5% classification. No trained ML model or LLM is used; no automatic resolution; the audit log is not tamper-proof; no customer validation or measured ROI. The cloud app has no authentication, so real financial data is prohibited.

## Pending before upload
- **Demo video (2–3 minutes): PENDING — not recorded.** Record it following the walkthrough in `04_Prototype_Readme_or_Link.md` and put it in `Appendix/Screenshots_or_Video/`.
- **06:** all fields are populated; contributions inferred from workstreams are labelled *Proposed contribution for member confirmation*. Each member confirms their section and gives a personal signature (status: typed name included; personal signature confirmation pending). If edited, regenerate: `src/render.sh 06_Individual_Contribution_Disclosure.md 06_Individual_Contribution_Statement.pdf` (run inside this folder).
- **05:** members may confirm their individual AI use (currently recorded as not separately logged).
- Open both Vercel links once before upload.
