/*
 * Retrieve badge information of the relevant users
*/
-- Retrieve relevant users
WITH _relevant_users AS (
    SELECT *
    FROM
        `deep-learning-438509.dim_stackoverflow_data_model.relevant_users`
),

-- Retrieve badge information from the last year
_badges AS (
    SELECT *
    FROM
        `bigquery-public-data.stackoverflow.badges` AS badges
    WHERE
        badges.date BETWEEN TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL @years_interval YEAR))
        AND TIMESTAMP(CURRENT_DATE())
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
        badges.tag_based AS badge_tag_based,
        # Compute the number of badges per user
        ROW_NUMBER() OVER (PARTITION BY users.id ORDER BY badges.date DESC) AS badge_rank
    FROM
        _relevant_users AS users
    LEFT JOIN _badges AS badges
        ON users.id = badges.user_id
)

-- Select only latest 3 badges per user
SELECT *
FROM _badges_relevant_users AS users_badge
WHERE
    users_badge.badge_name IS NOT NULL
    AND users_badge.badge_rank <= 3
