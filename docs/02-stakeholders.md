# 2. Stakeholders

> Illustrative roles for the scenario. They are not real people or an actual client.

## Stakeholder map

| Stakeholder | Role in the scenario | Interest | Influence | Engagement |
|-------------|---------------------|----------|-----------|------------|
| Demand planner | Calls the forecast daily to set orders | Accurate, fast forecasts that react to promotions | High | Co-define acceptance criteria; review sample forecasts |
| Store operations manager | Receives stock based on the plan | Fewer stock-outs and less waste | Medium | Informed of accuracy report |
| Data scientist / ML engineer | Maintains the model | Retrain easily, compare against baseline | Medium | Consulted on feature and validation requirements |
| Platform / IT operations | Runs the service | Health checks, logs, repeatable deployment | High | Consulted on non-functional requirements |
| Data governance lead | Owns data standards | Data lineage, no leakage, documented interfaces | Medium | Reviews the information-flow catalogue |
| Finance partner | Funds the work | Evidence of value against baseline | High | Informed of success measure BO-2 |

## Engagement approach

- **Manage closely (high influence):** demand planner, platform operations, finance partner. Requirements and acceptance criteria are agreed with these before build.
- **Keep satisfied / informed:** the rest receive the accuracy report and roadmap.

## Needs by stakeholder (feeds requirements)

| Stakeholder | Need | Becomes |
|-------------|------|---------|
| Demand planner | "Tell me tomorrow's units for store 3, product 7, on promo" | FR-01, FR-02 |
| Demand planner | "Don't let me type nonsense and get a number back" | FR-03 |
| Data scientist | "Show me whether the model beats last week's number" | FR-04, FR-07 |
| Platform operations | "Tell me it's alive and tell me when data has shifted" | FR-05, FR-08 |
| Data governance | "Prove the model never saw the answer" | FR-06 |
| Platform operations | "Every change must be built and tested before release" | NFR-01, NFR-02 |
