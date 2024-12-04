/*
 * Retrieve post answers of the relevant users in the last time frame from the latest post answer's creation date
 * NOTE: The latest post answer's creation date is 25/09/2022 (Checked on 04/12/2024
 * NOTE: 'owner_user_id' is the 'id' column of the user who posted the answer in the relevant_users table
 */
-- Retrieve relevant users
WITH _relevant_users AS (
    SELECT *
    FROM
        `deep-learning-438509.dim_stackoverflow_data_model.relevant_users`
),

-- Retrieve post answers in the last time frame from the latest post answer's creation date
_latest_posts_answers AS (
    SELECT *
    FROM
      `bigquery-public-data.stackoverflow.posts_answers` AS posts_answers
    WHERE
        -- Filter for time frame
        posts_answers.creation_date BETWEEN TIMESTAMP(DATE_SUB(DATE(2022, 11, 25), INTERVAL 4 MONTH)) AND TIMESTAMP(CURRENT_DATE())
        -- Filter for posts answers with required information
        AND posts_answers.body IS NOT NULL
        AND posts_answers.owner_user_id IS NOT NULL
        AND posts_answers.score IS NOT NULL
),

-- Filter for relevant users and add users information
_relevant_users_answers AS (
    -- TODO
)

-- Select only relevant information
-- TODO