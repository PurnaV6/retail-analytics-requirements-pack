# 3. Requirements and User Stories

Priority uses MoSCoW: **M**ust, **S**hould, **C**ould, **W**on't (this release).

## Functional requirements

| ID | Requirement | Priority | Objective |
|----|-------------|----------|-----------|
| FR-01 | The service shall return a forecast of units sold for a given store, product, date, price and promotion flag | M | BO-1 |
| FR-02 | The forecast shall be higher for a promoted day than for the same day without promotion | M | BO-3 |
| FR-03 | The service shall reject out-of-range input (unknown store or product, non-positive price) with a validation error and no forecast | M | BO-1 |
| FR-04 | The service shall publish the model's error and its improvement over the same-day-last-week baseline | M | BO-2 |
| FR-05 | The service shall report data drift between recent and historical data, per feature, with a status | S | BO-4 |
| FR-06 | Features shall be built so that no row uses information from its own future | M | BO-2 |
| FR-07 | The model shall be retrainable from the data with a single command that outputs the model and its metrics | M | BO-2, BO-5 |
| FR-08 | The service shall expose a health check | S | BO-5 |

## Non-functional requirements

| ID | Requirement | Priority | Objective |
|----|-------------|----------|-----------|
| NFR-01 | Every change shall be built, trained and tested automatically before it is accepted | M | BO-5 |
| NFR-02 | The service shall be packaged as a container image built automatically | S | BO-5 |
| NFR-03 | Every request shall be logged with a request ID, method, path, status and duration | S | BO-4, BO-5 |
| NFR-04 | Forecast requests should complete quickly enough for interactive use (target to be agreed with planners) | C | BO-1 |

## User stories and acceptance criteria

### US-01: Get a forecast (FR-01, FR-02)
**As a** demand planner **I want** tomorrow's unit forecast for a store and product, with promotion and price as inputs, **so that** I can set the order.

- **Given** store 1, product 1, a valid date, price 34.77 and no promotion, **when** I request a forecast, **then** I receive a non-negative number of units.
- **Given** the same request with promotion on and a lower price, **when** I request a forecast, **then** the forecast is higher than the unpromoted one.

### US-02: Be protected from bad input (FR-03)
**As a** demand planner **I want** invalid requests refused, **so that** I never act on a number produced from nonsense.

- **Given** store 99, **when** I request a forecast, **then** the request is rejected with a validation error.
- **Given** product 0, **when** I request a forecast, **then** the request is rejected with a validation error.
- **Given** a negative price, **when** I request a forecast, **then** the request is rejected with a validation error.

### US-03: See whether the model beats last week (FR-04, FR-07)
**As a** data scientist **I want** the error and baseline comparison published and the model retrainable in one step, **so that** I can show the model earns its place.

- **Given** a trained model, **when** I read the model information, **then** I see the error, the baseline error and a positive improvement figure.
- **Given** the data file, **when** I run the training command, **then** a model file and a metrics file are produced.

### US-04: Know when to distrust the forecast (FR-05)
**As a** platform operator **I want** a drift report by feature, **so that** I know when to retrain.

- **Given** two samples from the same distribution, **when** drift is calculated, **then** the status is "stable".
- **Given** a sample shifted well away from the reference, **when** drift is calculated, **then** the status is "significant drift".
- **Given** a feature missing from either sample, **when** drift is calculated, **then** that feature is skipped, not an error.

### US-05: Trust the model has not seen the answer (FR-06)
**As a** data governance lead **I want** proof that features use only past data, **so that** reported accuracy is honest.

- **Given** a daily series, **when** features are built, **then** a row's one-day lag is the previous day's value, not its own.
- **Given** warm-up rows with no history, **when** the training frame is built, **then** they are removed rather than filled.

### US-06: Release safely (NFR-01, NFR-02, FR-08)
**As a** platform operator **I want** each change built, trained, tested and packaged automatically, and a health check to call, **so that** releases are repeatable.

- **Given** a pushed change, **when** the pipeline runs, **then** it generates data, trains, runs the tests and builds the container image.
- **Given** a running service, **when** I call the health endpoint, **then** it reports "ok".
