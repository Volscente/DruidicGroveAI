v.1.0.1
-------
- [x] Add Module `bigquery_connector` in `src`
- [x] Add Pydantic Type `BigQueryClientConfig` in `src/types.py`
- [x] Add Function `_set_client` in `src/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add PyTest Fixture `fixture_bigquery_client_config` in `tests/conftest.py`
- [x] Add PyTest Fixture `fixture_bigquery_connector` in `tests/conftest.py`
- [x] Add PyTest `test_set_client` in `tests/test_bigquery_connector.py`
- [x] Add Function `read_file_from_path` in `src/general_utils/general_utils.py`
- [x] Add PyTest `test_read_file_from_path` in `tests/test_general_utils.py`
- [x] Add PyTest `test_read_file_from_path_exceptions`  in `tests/test_general_utils.py`
- [x] Add Function `_build_query_parameters` in `src/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add PyTest Fixture `fixture_dictionary_query_parameters` in `tests/conftest.py`
- [x] Add PyTest `test_build_query_parameters` in `tests/test_bigquery_connector.py`
- [x] Add Function `read_from_query_config` in `src/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add PyTest Fixture `fixture_query_config` in `tests/conftest.py`
- [x] Add PyTest `test_read_from_query_config` in `tests/test_bigquery_connector.py`

v.0.1.0
-------
- [x] Poetry init