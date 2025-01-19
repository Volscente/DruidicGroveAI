/*
 * Test query used in tests/test_data_preparation.py
 * as a test Input Table for Top Rarest Badges
 */
CREATE OR REPLACE TABLE `deep-learning-438509.dim_stackoverflow_data_model.test_top_rarest_badges` AS
-- Top Rarest Badge 1
SELECT
  'Python' AS badge_name,
  4200 AS badge_rarity,
UNION ALL
-- Top Rarest Badge 2
SELECT
  'HTML' AS badge_name,
  4129 AS badge_rarity,
UNION ALL
-- Top Rarest Badge 3
SELECT
  'AI' AS badge_name,
  3654 AS badge_rarity,
UNION ALL
-- Top Rarest Badge 4
SELECT
  'C++' AS badge_name,
  2497 AS badge_rarity,