# v.1.0.11

------

- [x] Add Query `raw_dataset.sql` in `queries/stackoverflow/data_preparation`
- [x] Add Pydantic Type `BigQueryQueryParameter` in `src/types.py`
- [x] Add Pydantic Type `BigQueryQueryConfig` in `src/types.py`
- [x] Add PyTest `test_bigquery_query_parameter` in `tests/test_types.py`
- [x] Add PyTest `test_bigquery_query_parameter_exceptions` in `tests/test_types.py`
- [x] Add PyTest `test_bigquery_query_config` in `tests/test_types.py`
- [x] Add PyTest `test_bigquery_query_config_exceptions` in `tests/test_types.py`
- [x] Add Function `_load_raw_dataset` in `src/data_preparation/data_preparation.StackOverflowDataPreparation`
- [x] Add Query  `test_raw_dataset.sql` in `queries/test_queries/stackoverflow_data_preparation`
- [x] Add PyTest Fixture `fixture_raw_dataset_config` in `tests/conftest.py`
- [x] Add PyTest `test_load_raw_dataset` in `tests/test_data_preparation.py`
- [x] Refactor PyTest `test_load_input_tables` in `tests/test_data_preparation.py`

# v.1.0.10

------

- [x] Add Function `wrap_dictionary_to_query_config` in `src/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add PyTest `test_wrap_dictionary_to_query_config` in `tests/test_bigquery_connector.py`
- [x] Refactor Notebook `stackoverflow_eda.ipynb` in `notebooks/stackoverflow/eda`


# v.1.0.9

------

- [x] Add Query `test_create_table.sql` in `queries/test_queries/bigquery_connector`
- [x] Add Module `data_preparation` in `src`
- [x] Add Class `StackOverflowDataPreparation` in `src/data_preparation/data_preparation.py`
- [x] Add Function `_load_input_tables` in `src/data_preparation/data_preparation.StackOverflowDataPreparation`
- [x] Add Query `test_users_information.sql` in `queries/test_queries/stackoverflow_data_preparation`
- [x] Add Query `test_top_rarest_badges.sql` in `queries/test_queries/stackoverflow_data_preparation`
- [x] Add Query `test_post_answers.sql` in `queries/test_queries/stackoverflow_data_preparation`
- [x] Add PyTest Fixture `fixture_stackoverflow_data_preparation` in `tests/conftest.py`
- [x] Add PyTest `test_load_input_tables` in `tests/test_data_preparation.py`
- [x] Add Query `top_rarest_badges.sql` in `queries/stackoverflow/data_preparation`
- [x] Add Query `users_information.sql` in `queries/stackoverflow/data_preparation`
- [x] Add Query `post_answers.sql` in `queries/stackoverflow/data_preparation`


# v.1.0.8

------

- [x] Add Function `table_exists` in the class `src/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Add PyTest `test_table_exists` in `tests/test_bigquery_connector.py`

# v.1.0.7

------

- [x] Refactor Function `read_from_query_config` in `src/bigquery_connector/bigquery_connector.BigQueryConnector`
- [x] Refactor PyTest Fixture `fixture_query_config` in `tests/conftest.py`
- [x] Add PyTest Fixture `fixture_create_table_query_config`  in `tests/conftest.py`
- [x] Refactor PyTest `test_read_from_query_config` in `tests/test_bigquery_connector.py`
- [x] Change used functions in `notebooks/stackoverflow/eda/stackoverflow_eda.ipynb`

# v.1.0.6

------

- [x] Add Section `General` in Document `docs/stackoverflow_answer_score_classification/development_v.1.0.x.html`
- [x] Add Section `Input Tables` in Document `docs/stackoverflow_answer_score_classification/development_v.1.0.x.html`
- [x] Add Section `Data Preparation` in Document `docs/stackoverflow_answer_score_classification/development_v.1.0.x.html`
- [x] Add Section `Training Dataset` in Document `docs/stackoverflow_answer_score_classification/development_v.1.0.x.html`

# v.1.0.5

------

- [x] Add Query `post_answers_relevant_users.sql` in `queries/stackoverflow/eda/posts_answers`
- [x] Add Section `Post Answers` in Notebook `notebooks/stackoverflow/eda/stackoverflow_eda.ipynb`
- [x] Add Section `Post Answers` in Document `docs/stackoverflow_answer_score_classification/exploratory_data_analysis.html`

# v.1.0.4

------

- [x] Add Document `index.html` in `docs`
- [x] Add Document `use_cases.html` in `docs`
- [x] Add Document `general.html` in `docs/stackoverflow_answer_score_classification`
- [x] Add Document `style.css` in `docs`
- [x] Add Navigation in `style.css`
- [x] Add Document `exploratory_data_analysis.html` in `docs/stackoverflow_answer_score_classification`
- [x] Add Document `development_v.1.0.x.html` in `docs/stackoverflow_answer_score_classification`
- [x] Add Document `input_data_sources.html` in `docs/stackoverflow_answer_score_classification`

# v.1.0.3

------

- [x] Add Query `relevant_users_view.sql` in `queries/stackoverflow/eda/views`
- [x] Add Query `badges_relevant_users.sql` in `queries/stackoverflow/eda/badges`
- [x] Add Query `number_badges_relevant_users.sql` in `queries/stackoverflow/eda/badges`
- [x] Update Notebook `stackoverflow_eda.ipynb` in `notebooks/stackoverflow/eda` by adding the section `Badges`

# v.1.0.2

-------

- [x] Add Query `relevant_users.sql` in `queries/stackoverflow/eda/users`
- [x] Add Notebook `stackoverflow_eda` in `notebooks/stackoverflow/eda`

# v.1.0.1

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

# v.0.1.0

-------

- [x] Poetry init