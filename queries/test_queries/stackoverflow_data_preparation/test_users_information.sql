/*
 * Test query used in tests/test_data_preparation.py
 * as a test Input Table for Users Information
 */
CREATE OR REPLACE TABLE `deep-learning-438509.dim_stackoverflow_data_model.test_users_information` AS
-- User 1
SELECT
  1 AS user_id,
  'Kyoraku Shunsui' AS user_name,
  'I am a professional Python developer with 10+ years of experience.' AS user_about_me,
  TIMESTAMP('2012-01-01 15:25:59') AS user_creation_date,
  'Japan' AS user_location,
  2500 AS user_reputation,
  300 AS user_up_votes,
  90 AS user_down_votes,
  425 AS user_views,
  'https://i.stack.imgur.com/l2vFZ.png?s=135&g=1' AS user_profile_image_url,
  'https://groups.google.com/group/some_group' AS user_website_url,
  200 AS badge_count,
  ? AS badges_list

UNION ALL

-- User 2
SELECT
    2 AS id,
    'test_2' AS display_name