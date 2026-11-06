# Wireframes / screen layouts

These layouts were implemented directly. The screenshots in `../Screenshots_or_Video/` are the high-fidelity versions.

```
┌ Sidebar (desktop) ─┐┌ Top bar: mode badge · active run selector · analyst name ───────────────┐
│ Command Centre     ││                                                                          │
│ Data & Recon Studio││  SCREEN CONTENT                                                          │
│ Investigation      ││                                                                          │
│ Simulator          ││                                                                          │
│ Prevention & Audit ││                                                                          │
└────────────────────┘└──────────────────────────────────────────────────────────────────────────┘
Mobile: sidebar → bottom tab bar (5 icons); grids collapse to 1–2 columns.
```

**1 · Command Centre**
```
[ 8 KPI tiles: total · matched · unmatched · breaks · high-risk · match rate · break rate · exposure ]
[ Breaks by classification (bar) ][ Recurring break trends by cycle (stacked bar, 2 cols)      ]
[ Source-system performance      ][ Resolution performance ][ Top recurring patterns          ]
[ Highest-exposure open breaks                ][ Recent activity (audit)                      ]
```
**2 · Data & Reconciliation Studio**
```
[ Sample datasets: ( Nexora Global | Indian Banking ) toggle ]
[   Nexora: cycle · count · Load · Load & run · downloads (CSV/XLSX per source, history, rules) ]
[   Indian: Load into all sources · Load & run · invalid-row count · downloads (3 sources + answer key) · scenario list ]
[ Ledger upload card ][ Bank upload card ][ Gateway upload card ]  → preview · mapping · validation · confirm
[ Run reconciliation: tolerances + label ][ Run history table (select active)                   ]
[ Summary KPIs ] [ Breaks by type ][ Engine validation vs ground truth + confusion table ]
[ Matched transactions (lazy, filter, paginate) ]
```
**3 · Investigation Workbench**
```
[ Filters: search · type · risk · status · root cause · recurrence · sort ]
[ Break table (paginated) ] │ [ Header: type · explanation · status · risk · variance · confidence ]
                            │ [ Transaction legs side by side (diffs highlighted)                 ]
                            │ [ BREAK DNA panel: code · fingerprint strip · 10 features           ]
                            │ [ Root cause · evidence (rule IDs) · confidence breakdown · risk    ]
                            │ [ Similar historical cases (similarity bars, why similar/differs)   ]
                            │ [ Next best action · alternative · decision form · history          ]
```
**4 · Resolution Simulator**
```
[ Estimates disclaimer ]
[ Break selector + scenario toggles ][ Current situation + proposed resolution        ]
[ Hold ][ Retry ][ Escalate ][ Correct reference ][ Investigate ]   ← side-by-side scenario cards
[ Comparison chart (clearance % vs hours) ][ Documented assumptions ]
```
**5 · Prevention & Audit Centre**
```
[ Signature finding callout (top chronic systemic pattern, computed)                      ]
[ Radar chart: families latest vs historical ][ Recurring patterns table with trend bars  ]
[ Preventive recommendations ][ Common root causes ]
[ Source-system issue distribution ][ Historical resolution outcomes ]
[ HITL KPIs: decisions · acceptance · override · avg investigation · false resolution · recurring ]
[ Repeated break tracking ][ Audit log (filter, CSV export) ]
```
