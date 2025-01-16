/*
 * Test query used in tests/test_data_preparation.py
 * as a test Input Table
 */
CREATE OR REPLACE TABLE `deep-learning-438509.dim_stackoverflow_data_model.test_input_table_1` AS
SELECT
  @id AS id,
  @display_name AS display_name