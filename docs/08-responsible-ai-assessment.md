# 8. Responsible AI Assessment

> Scenario assessment of the forecasting model in
> [retail-demand-forecast-api](https://github.com/PurnaV6/retail-demand-forecast-api).
> Numbers were measured by running the committed model over the held-out final 8
> weeks (2,800 store-product-days, synthetic data). This is a self-assessment
> written for a portfolio, not an external audit.

## 1. Purpose and intended use

Advisory next-day unit forecasts for store-product pairs, used by demand planners
as one input to ordering. **Not intended** for staffing or pay decisions, for
anything about individual people, or for automatic ordering without human review.

## 2. Data and privacy

- The data is synthetic: store, product, date, price, promotion flag and units. It contains **no personal data**, so no privacy harm arises in this project.
- In a real deployment, sales aggregated by store and product are normally not personal data, but if the feed were built from loyalty-card or customer-level records, a data protection impact assessment under UK GDPR would be needed first. The interface catalogue (doc 5) deliberately specifies store-level aggregates only.

## 3. Performance across groups

A single accuracy figure can hide a model that works for some groups and not others.
Measured on the held-out period:

### By store

| Store | Mean daily units | Model error | Baseline error | Model error as % of mean |
|-------|-----------------|-------------|----------------|--------------------------|
| 1 | 114.5 | 12.56 | 26.93 | 11.0% |
| 2 | 44.6 | 5.07 | 9.82 | 11.4% |
| 3 | 50.9 | 5.64 | 10.04 | 11.1% |
| 4 | 69.3 | 7.89 | 15.94 | 11.4% |
| 5 | 91.8 | 9.38 | 20.95 | 10.2% |

**Finding:** relative error is consistent across stores (10.2% to 11.4%), and the model
beats the baseline in every store. No store is systematically under-served.

### Promotion days versus normal days

| Day type | Rows | Model error | Baseline error |
|----------|------|-------------|----------------|
| Normal | 2,575 | 7.15 | 13.49 |
| Promotion | 225 | 19.12 | 53.82 |

**Finding:** promotion days are about 2.7 times harder to forecast (19.12 vs 7.15) even
though the model is far better than the baseline there. Planners should treat
promotion-day forecasts as less certain. This is a documented limitation, and a
reason to add forecast ranges (roadmap candidate), not just point forecasts.

### Bias

Mean forecast minus mean actual is +0.08 units, so there is no meaningful systematic
over- or under-forecasting.

## 4. Transparency and explainability

The model is a gradient-boosted tree, and its inputs are plain business features.
Share of the model's learned importance (gain):

| Feature | Share |
|---------|-------|
| 28-day rolling average of sales | 65.4% |
| Promotion flag | 13.1% |
| 7-day rolling average | 8.0% |
| Day of week | 5.7% |
| Sales 7 days ago | 2.5% |

**Reading it:** the model leans mainly on recent sales level and on promotions, which is
what a planner would expect. Nothing surprising or opaque drives the output. This
shows which features matter overall, not why one particular forecast was produced.

## 5. Human oversight

- Forecasts are advisory; the planner decides the order.
- Out-of-range inputs are refused rather than answered (FR-03).
- A drift report (FR-05) tells operators when the data has moved away from what the model learned, which is the trigger to review before trusting it.

## 6. Limitations stated plainly

1. Trained and tested on synthetic data, so accuracy says nothing about a real retailer.
2. One-day horizon only.
3. No knowledge of events the data does not contain (weather, local events, supply disruption, competitor pricing).
4. Promotion days are less accurate (section 3).
5. Fairness checks here cover stores and promotion status only; a real deployment would also need to check any other segments that matter to the business.

## 7. Risks and mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Over-reliance on the forecast | Medium | Stock-outs or waste | Advisory framing; show uncertainty on promotion days |
| Silent accuracy loss as demand shifts | Medium | Poor ordering | Drift monitoring; monthly error review |
| Data leakage inflates reported accuracy | Low | Misleading results | Leakage tests (FR-06) |
| Personal data enters the feed later | Low | Legal exposure | Store-level aggregates only; DPIA before any change |

## 8. Accountability

| Responsibility | Owner (scenario roles) |
|----------------|-----------------------|
| Model accuracy and retraining | Data scientist |
| Service availability | Platform operations |
| Data feed and its quality | Data governance lead |
| Decision to order | Demand planner |
