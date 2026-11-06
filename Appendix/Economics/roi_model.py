# Illustrative ROI model. Every input is an ASSUMPTION, not customer data.
S = [  # name, breaks/month, minutes/break, analyst INR/hr, time saved %, hosting INR/mo, support+rules FTE, FTE cost INR/mo
 ("A · Co-operative bank (small)",  2000, 20, 500, 0.20,  15000, 0.25, 120000),
 ("B · NBFC / mid-size bank",      10000, 20, 650, 0.25,  40000, 0.50, 120000),
 ("C · Payments ops (large)",      40000, 15, 800, 0.30, 120000, 1.00, 120000),
]
rows=[]
for n,b,m,c,s,h,f,fc in S:
    hrs=b*m/60; cost=hrs*c; saved_h=hrs*s; saved=saved_h*c; ops=h+f*fc; net=saved-ops
    be=ops/cost  # break-even time-saving share
    rows.append((n,b,m,c,s,hrs,cost,saved_h,saved,h,f*fc,ops,net,be))
def inr(x): return f"₹{x:,.0f}"
print("| Scenario | Breaks/month* | Min per break* | Analyst ₹/hr* | Manual hours/month | Manual cost/month | Time saved* | Hours saved | Value of time saved | Hosting* | Support & rule upkeep* | Platform operating cost | Net operational saving/month | Break-even time saving |")
print("|"+"---|"*14)
for r in rows:
    n,b,m,c,s,hrs,cost,sh,sv,h,sup,ops,net,be=r
    print(f"| {n} | {b:,} | {m} | {c} | {hrs:,.0f} | {inr(cost)} | {s:.0%} | {sh:,.0f} | {inr(sv)} | {inr(h)} | {inr(sup)} | {inr(ops)} | {inr(net)} | {be:.1%} |")
