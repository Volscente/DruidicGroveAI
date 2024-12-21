/*
 * Test query used in tests/test_bigquery_connector.py
 */
CREATE OR REPLACE TABLE `your_project_id.your_dataset_id.test_table_creation` AS
SELECT
  @id AS id,
  @display_name AS display_name;

