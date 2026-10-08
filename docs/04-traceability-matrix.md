# 4. Requirements Traceability Matrix

Links each requirement to the story that describes it, the code that implements
it and the test that proves it. Repository referenced:
`retail-demand-forecast-api`. Run `check_traceability.py` to confirm every file
and test below exists.

| Req | Story | Implemented in | Verified by | Status |
|-----|-------|----------------|-------------|--------|
| FR-01 | US-01 | `api/main.py`, `src/predict.py` | `tests/test_api.py::test_predict_valid_request` | Verified |
| FR-02 | US-01 | `src/features.py`, `src/predict.py` | `tests/test_api.py::test_predict_promo_increases_prediction_vs_no_promo` | Verified |
| FR-03 | US-02 | `api/schemas.py` | `tests/test_api.py::test_predict_rejects_out_of_range_inputs` (3 cases) | Verified |
| FR-04 | US-03 | `src/train.py`, `api/main.py` | `tests/test_api.py::test_model_info` | Verified |
| FR-05 | US-04 | `src/monitoring.py`, `api/main.py` | `tests/test_monitoring.py::test_identical_distributions_report_stable`, `tests/test_monitoring.py::test_shifted_distribution_reports_drift`, `tests/test_monitoring.py::test_missing_column_is_skipped_not_errored`, `tests/test_api.py::test_monitor_drift` | Verified |
| FR-06 | US-05 | `src/features.py` | `tests/test_features.py::test_lag_features_do_not_leak_future_values`, `tests/test_features.py::test_build_training_frame_drops_warmup_rows_and_has_no_lag_nans`, `tests/test_features.py::test_build_inference_row_produces_expected_columns` | Verified |
| FR-07 | US-03 | `src/train.py` | `tests/test_train.py::test_train_model_runs_end_to_end_and_beats_naive_baseline` | Partly verified (see gap 1) |
| FR-08 | US-06 | `api/main.py` | `tests/test_api.py::test_health` | Verified |
| NFR-01 | US-06 | `.github/workflows/ci.yml` | CI run on every push (generate data, train, test) | Verified by CI |
| NFR-02 | US-06 | `Dockerfile`, `docker-compose.yml` | CI `docker build` step | Verified by CI |
| NFR-03 | n/a | `api/main.py` (request-logging middleware) | Observed in server logs; no automated test | Gap 2 |
| NFR-04 | n/a | n/a | Latency observed at roughly 30-170 ms per request locally; no target agreed, no test | Gap 3 |

## Coverage summary

- 15 automated tests in the forecasting repo; each is referenced above (the three
  out-of-range cases count as one parametrised test).
- 8 functional requirements: 7 fully verified, 1 partly.
- 4 non-functional requirements: 2 verified by the CI pipeline, 2 with gaps.

## Gaps found by doing this exercise

1. **FR-07:** the training test confirms the pipeline runs and writes a model and metrics, but does not assert that the model beats the baseline. That is only checked indirectly through `test_model_info`, which asserts a positive improvement on the committed model. *Action: add an assertion on the toy-data run, or a regression test on the real metrics file.*
2. **NFR-03:** logging is implemented but untested. *Action: add a test that a request produces a log line with a request ID.*
3. **NFR-04:** no latency target was ever agreed with the planners, so there is nothing to test against. *Action: agree a target (stakeholder decision), then add a timing test.*

These are carried into the [roadmap](06-product-roadmap.md) as item R0.
