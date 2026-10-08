# Retail Demand Forecasting Platform: Business Analysis Pack

A business analysis pack for the [Retail Demand Forecasting API](https://github.com/PurnaV6/retail-demand-forecast-api):
the requirements, stakeholder map, acceptance criteria, traceability matrix,
information-flow catalogue and product roadmap that sit around a data product.

**This is a portfolio project, not client work.** The stakeholders, objectives
and roadmap are an illustrative scenario written against my own open-source
project. What is real: every requirement is traced to code in that repo and to
an automated test that exists, and the matrix says plainly where a requirement
has no test.

## What is in the pack

| # | Document | What it shows |
|---|----------|---------------|
| 1 | [Business requirements](docs/01-business-requirements.md) | Context, objectives, scope, assumptions, constraints, success measures |
| 2 | [Stakeholders](docs/02-stakeholders.md) | Stakeholder map, interests, and how each is engaged |
| 3 | [Requirements and user stories](docs/03-requirements-and-user-stories.md) | Functional and non-functional requirements, MoSCoW priority, Given/When/Then acceptance criteria |
| 4 | [Traceability matrix](docs/04-traceability-matrix.md) | Requirement -> story -> implementation -> test, with coverage gaps |
| 5 | [Information flows](docs/05-information-flows.md) | Interface catalogue and data-flow diagram for supply and demand information |
| 6 | [Product roadmap](docs/06-product-roadmap.md) | Delivered, next and later items with priorities, dependencies, acceptance criteria and intended outcomes |
| 7 | [Options, feasibility, impact and business case](docs/07-options-feasibility-and-business-case.md) | Weighted options analysis, feasibility and impact assessments, value estimation with stated assumptions, outcome measures, delivery-method comparison |
| 8 | [Responsible AI assessment](docs/08-responsible-ai-assessment.md) | Privacy, error measured by store and by promotion status, bias, transparency, human oversight, limitations, accountability |

## Why a pack like this matters

A model that works is not a delivered product. Someone has to agree what
"works" means, who depends on it, what data it needs and from where, how each
requirement will be proven, and what comes next and in what order. These
documents are that layer.

## Checking the traceability

`check_traceability.py` parses the matrix and fails if any referenced test or
file does not exist in the forecasting repo, so the traceability cannot drift
silently.

```bash
python check_traceability.py /path/to/retail-demand-forecast-api
```
