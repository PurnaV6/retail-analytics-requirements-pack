# 1. Business Requirements

> Illustrative scenario for portfolio purposes.

## Context

A regional retailer with 5 stores and a 10-product core range plans
replenishment from last week's sales. Promotions cause stock-outs and
over-ordering because the plan does not react to them. Planners want a
next-day unit forecast per store and product that they can call from their
planning tools, and that tells them when it can no longer be trusted.

## Objectives

| ID | Objective | Measure of success |
|----|-----------|--------------------|
| BO-1 | Give planners a store/product/day demand forecast on request | Forecast returned for any valid store, product and date |
| BO-2 | Forecast must be better than the current practice ("same as last week") | Model error is lower than the same-day-last-week baseline, published with the service |
| BO-3 | Forecast must respond to promotions and price | A promoted day forecasts higher than the same day unpromoted |
| BO-4 | Planners must know when the forecast may no longer be reliable | Data-drift status available on demand |
| BO-5 | The service must be repeatable and safe to change | Every change is built, tested and packaged automatically |

## Scope

**In scope:** next-day unit forecast per store/product; accuracy reporting against the
baseline; drift monitoring; automated build, test and packaging.

**Out of scope (this release):** authentication and user management; real-time
streaming data; forecast horizons beyond one day; automatic replenishment orders;
connection to a live point-of-sale system.

## Assumptions

- A1: History of daily units, price and promotion flag per store/product is available. *(In this project: a synthetic dataset, so no real data was needed.)*
- A2: Planners call the forecast from other tools over HTTP, so an API is the right interface.
- A3: A weekly view of accuracy is enough; there is no intraday requirement.

## Constraints

- C1: No real retail data was used. Quoted accuracy applies to synthetic data and says nothing about a real retailer.
- C2: The service runs on a single container; no high-availability requirement in this release.

## Success measure actually achieved

On the held-out final 8 weeks of the synthetic dataset, the model's mean absolute
error was 8.11 units against 16.74 for the same-day-last-week baseline, a 51.5%
reduction (`models/metrics.json` in the forecasting repo).

## Risks

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Future information leaks into features, inflating accuracy | Forecast looks good in testing, fails in use | Lag features built so a row cannot see its own future; covered by tests |
| Demand pattern shifts after launch | Silent loss of accuracy | Drift endpoint (BO-4) |
| Synthetic data hides real-world messiness | Accuracy overstated | Stated as constraint C1; roadmap item R2 adds data-quality checks on real feeds |
