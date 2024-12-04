/*
 * Retrieve post answers of the relevant users in the last time frame from the latest post answer's creation date
 * NOTE: The latest post answer's creation date is 25/09/2022 (Checked on 04/12/2024)
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
        posts_answers.creation_date BETWEEN TIMESTAMP(DATE_SUB(DATE(2022, 11, 25), INTERVAL @months_interval MONTH)) AND TIMESTAMP(CURRENT_DATE())
        -- Filter for posts answers with required information
        AND posts_answers.body IS NOT NULL
        AND posts_answers.owner_user_id IS NOT NULL
        AND posts_answers.score IS NOT NULL
)

-- Filter for relevant users and add users information
SELECT
    posts_answers.title AS answer_title,
    posts_answers.body AS answer_body,
    posts_answers.answer_count,
    posts_answers.comment_count AS answer_comment_count,
    posts_answers.creation_date AS answer_creation_date,
    posts_answers.favorite_count AS answer_favorite_count,
    posts_answers.view_count AS answer_view_count,
    posts_answers.tags AS answer_tags,
    users.display_name AS user_display_name,
    users.about_me AS user_about_me,
    users.creation_date AS user_creation_date,
    users.last_access_date AS user_last_access_date,
    users.location AS user_location,
    users.reputation AS user_reputation,
    users.up_votes AS user_up_votes,
    users.down_votes AS user_down_votes,
    users.views AS user_views,
    posts_answers.score AS answer_score
FROM
    _latest_posts_answers AS posts_answers
INNER JOIN _relevant_users AS users
    ON posts_answers.owner_user_id = users.id
