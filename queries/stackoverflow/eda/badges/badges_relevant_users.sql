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
        users.id AS user_id,
        users.display_name AS user_name,
        users.about_me AS user_about_me,
        users.creation_date AS user_creation_date,
        users.last_access_date AS user_last_access_date,
        users.location AS user_location,
        users.reputation AS user_reputation,
        users.up_votes AS user_up_votes,
        users.down_votes AS user_down_votes,
        users.views AS user_views,
        users.profile_image_url AS user_profile_image_url,
        users.website_url AS user_website_url,
        badges.name AS badge_name,
        badges.date AS badge_date,
        badges.class AS badge_class,
        badges.tag_based AS badge_tag_based
    FROM
        _badges AS badges
    INNER JOIN _relevant_users AS users
        ON badges.user_id = users.id
)

-- Select all the badge information retrieve
SELECT *
FROM _badges_relevant_users
