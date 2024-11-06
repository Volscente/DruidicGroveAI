/*
 * Retrieve badge information of the relevant users
*/
-- Retrieve relevant users
WITH _relevant_users AS (
    SELECT *
    FROM
        `deep-learning-438509.dim_stackoverflow_data_model.relevant_users`
),

-- Retrieve badge information
_badges AS (
    SELECT *
    FROM
        `bigquery-public-data.stackoverflow.badges`
),

-- Retrieve badge information of relevant users
_badges_relevant_users AS (
    SELECT
        users.*,
        badges.name AS badge_name,
        badges.date AS badge_date,
        badges.class AS badge_class,
        badges.tag_based AS badge_tag_based
    FROM
        _badges as badges
    INNER JOIN _relevant_users AS users
        ON badges.user_id = users.id
)

-- Select all the badge information retrieve
# TODO: Investigate count of _relevant_users and _badges_relevant_users
SELECT *
FROM _badges_relevant_users

