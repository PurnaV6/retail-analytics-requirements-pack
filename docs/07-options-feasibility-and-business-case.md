# 7. Options Analysis, Feasibility, Impact Assessment and Business Case

> Illustrative scenario for portfolio purposes. Figures marked **measured** come
> from the forecasting repo's held-out test period (synthetic data). Figures
> marked **assumed** are placeholders to demonstrate the method; a real business
> case would replace them with the finance partner's numbers.

## 1. Decision to be made

How should the retailer produce next-day demand forecasts for 5 stores and 10
products, given that "same as last week" is the current practice and misses
promotions?

## 2. Options analysis

| Option | Description |
|--------|-------------|
| A | Do nothing: keep using last week's sales as the forecast |
| B | Spreadsheet moving average maintained by planners |
| C | Buy a vendor forecasting tool (hypothetical; no vendor was assessed) |
| D | Build and run the in-house service described in this pack (delivered) |

### Criteria and weights (set before scoring)

| Criterion | Weight | Why it matters |
|-----------|--------|----------------|
| Forecast accuracy | 30% | Drives the benefit |
| Reacts to promotions | 20% | The stated pain point |
| Time to value | 15% | Cost of waiting |
| Running cost | 10% | Ongoing spend |
| Transparency and control | 15% | Planners must trust and challenge the number |
| Delivery risk | 10% | Chance of not working as promised |

### Scores (1 = poor, 5 = strong; analyst judgement, with the basis stated)

| Criterion | A | B | C | D | Basis |
|-----------|---|---|---|---|-------|
| Accuracy | 1 | 2 | 4 | 4 | D **measured**: error 8.11 vs 16.73 baseline units. C **assumed**, not tested |
| Promotions | 1 | 1 | 4 | 4 | D **measured**: promo-day error 19.1 vs 53.8 for baseline. B ignores promotions by design |
| Time to value | 5 | 4 | 3 | 4 | D already built; C needs procurement and onboarding |
| Running cost | 5 | 5 | 2 | 4 | C carries licence fees; D is one container |
| Transparency | 5 | 5 | 2 | 4 | C is typically a black box; D's features are inspectable |
| Delivery risk | 5 | 4 | 3 | 3 | D has never run on real data |

### Weighted result

| Option | Weighted score |
|--------|----------------|
| **D Build** | **3.90** |
| C Buy | 3.25 |
| B Spreadsheet | 3.05 |
| A Do nothing | 3.00 |

**Sensitivity:** with equal weights, D is still first (3.83), but A rises to 3.67. The
case for D therefore rests on accuracy and promotion handling mattering more than
the other criteria, which is exactly what the measured results support.

**Recommendation:** D, piloted on one store first (see section 6). C is not ruled
out; it simply was never tested, so its scores are the weakest evidence here.

## 3. Feasibility assessment

| Dimension | Assessment | Evidence | Rating |
|-----------|-----------|----------|--------|
| Technical | Model trains, serves and is monitored | 15 automated tests, CI pipeline | Feasible |
| Data | Depends on a clean daily feed (IF-01) | Only synthetic data used | **Unproven**: largest risk |
| Operational | One container, no high availability | Dockerfile built in CI | Feasible with risk |
| Organisational | Planners must change how they order | No user trial run | Unproven |
| Financial | Low build and run cost | See section 5 | Feasible |

## 4. Impact assessment

| Group affected | Impact | Direction | Mitigation |
|----------------|--------|-----------|-----------|
| Demand planners | Daily workflow changes to use a forecast | Mixed | Pilot on one store; planners can override |
| Store operations | Different stock arrives | Positive if accuracy holds | Report accuracy monthly |
| IT operations | One more service to run and monitor | Negative (workload) | Health check, drift report, CI |
| Data governance | New data flows and a model to govern | Neutral | Interface catalogue (doc 5) and responsible-AI assessment (doc 8) |
| Customers | Better availability on promoted items | Positive | Track stock-out rate once real data exists |

## 5. Value estimation (method with assumed inputs)

**Measured:** average error falls from 16.73 to 8.11 units per store-product-day, so
8.63 units of error are avoided per series-day. With 50 series (5 stores x 10 products)
over 365 days = 18,250 series-days, that is **about 157,000 units of avoided forecast
error per year**.

**Assumed:** the cost of one unit of forecast error (waste plus lost margin). The
true figure is unknown, so the estimate is shown as a range.

| Assumed cost per unit of error | Gross annual value | After assumed run cost of 600 per year |
|--------------------------------|-------------------|----------------------------------------|
| 0.25 | about 39,400 | about 38,800 |
| 0.50 | about 78,700 | about 78,100 |
| 1.00 | about 157,400 | about 156,800 |

**Reading this honestly:** error reduction does not turn into money one for one. If
only 30% of it is realised in better ordering, the middle row falls to about 23,600
a year. The useful conclusion is not the number but the **break-even**: the service
pays for its assumed run cost if each unit of error costs more than about 0.004.
The decision is therefore not sensitive to the assumption, but the real figure should
still be obtained before committing.

## 6. Business case summary

| | |
|---|---|
| **Proposal** | Adopt option D, piloted on one store for 8 weeks, then extend |
| **Costs** | Build effort already spent; assumed run cost 600 per year |
| **Benefits** | About 157,000 units of avoided forecast error a year at full rollout (measured on synthetic data); money value to be confirmed |
| **Key risks** | No real data tested; planner adoption; accuracy on real, messier demand |
| **Decision requested** | Approve the pilot and the real data feed (roadmap R2) |
| **Go / no-go test** | Pilot error must beat the same-day-last-week baseline on real data |

### How outcomes will be measured

| Measure | How | Frequency |
|---------|-----|-----------|
| Error against baseline | `/model/info` metrics on held-out weeks | Monthly |
| Promotion-day error | Same metrics, promo days only | Monthly |
| Forecast bias | Mean forecast minus mean actual | Monthly |
| Data drift | `/monitor/drift` | Weekly |
| Planner adoption | Share of orders placed using the forecast | Pilot period |
| Stock-outs and waste | Store operations data (needs real feed) | Pilot period |

## 7. Comparing delivery methods

| Method | Strengths | Weaknesses | Fit here |
|--------|-----------|-----------|----------|
| One full release | Single cut-over | No early feedback; the data risk surfaces last | Poor |
| Iterative releases following the roadmap (R0 to R6) | Early feedback; riskiest item (real data) tackled first | Needs ongoing planner time | **Recommended** |
| Pilot first, then iterate | Real evidence before scaling | Slower rollout | **Recommended as the first step** |
