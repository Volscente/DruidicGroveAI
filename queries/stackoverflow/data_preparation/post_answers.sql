/*
 * Create a table including information from post answers for users in the table
 * deep-learning-438509.curated_stackoverflow_data_model.users_information.
 * They are retrieve from the latest post answer's creation date
 * and @months_interval months before.
 * NOTE: The latest post answer's creation date is 25/09/2022 (Checked on 04/12/2024)
 * NOTE: 'owner_user_id' is the 'id' column of the user who posted the answer
 */
CREATE OR REPLACE TABLE `deep-learning-438509.curated_stackoverflow_data_model.post_answers` AS

-- Retrieve relevant users IDs
WITH _users AS (
    SELECT user_id
    FROM
        `deep-learning-438509.curated_stackoverflow_data_model.users_information`
),

-- Retrieve post answers for the relevant users
_post_aswers AS (
    SELECT
        posts_answers.owner_user_id AS answer_user_id,
        posts_answers.body AS answer_body,
        posts_answers.comment_count AS answer_comment_count,
        posts_answers.creation_date AS answer_creation_date,
        posts_answers.score AS answer_score
    FROM
        `bigquery-public-data.stackoverflow.posts_answers` AS posts_answers
    WHERE
        posts_answers.owner_user_id IN (SELECT users.user_id FROM _users AS users)
)

-- Filter just for the last @