/*
 * Test query used in tests/test_data_preparation.py
 * as a test Input Table for Users Information
 */
CREATE OR REPLACE TABLE `deep-learning-438509.dim_stackoverflow_data_model.test_post_answers` AS

-- Retrieve users
WITH _users AS (
    SELECT user.user_id
    FROM
        `deep-learning-438509.dim_stackoverflow_data_model.test_users_information` AS user
),

-- Define test post answers
_post_answers AS (
    -- Post Answer 1
    SELECT
        1 AS answer_user_id,
        "Have you tried turn it off and on again?" AS answer_body,
        2 AS answer_comment_count,
        TIMESTAMP("2013-06-21 12:00:19") AS answer_creation_date,
        0.6 AS answer_score
    UNION ALL
    -- Post Answer 2
    SELECT
        3 AS answer_user_id,
        "Maybe you want to create a sub-procedure for this? Try with bash!" AS answer_body,
        3 AS answer_comment_count,
        TIMESTAMP("2015-03-14 17:07:01") AS answer_creation_date,
        0.2 AS answer_score
    UNION ALL
    -- Post Answer 3
    SELECT
        2 AS answer_user_id,
        "The error is due to the Docker image python:3.9.20, which has a critical vulnerability." AS answer_body,
        5 AS answer_comment_count,
        TIMESTAMP("2019-09-14 23:59:59") AS answer_creation_date,
        1.0 AS answer_score
)

-- Filter post answers by the IDs in test_users_information
SELECT *
FROM
    _post_answers
WHERE
    answer_user_id IN (SELECT user_id FROM _users)
