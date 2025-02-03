/*
 * Create a table by joining the following input tables for the StackOverflow use case:
 * 1. `deep-learning-438509.curated_stackoverflow_data_model.users_information`
 * 2. `deep-learning-438509.curated_stackoverflow_data_model.top_rarest_badges`
 * 3. `deep-learning-438509.curated_stackoverflow_data_model.post_answers`
 */
CREATE OR REPLACE TABLE `deep-learning-438509.curated_stackoverflow_data_model.raw_dataset` AS
-- Retrieve users information
WITH _users AS (
    SELECT *
    FROM
        `deep-learning-438509.curated_stackoverflow_data_model.users_information`
),

-- Retrieve top rarest badges
_badges AS (
    SELECT *
    FROM
        `deep-learning-438509.curated_stackoverflow_data_model.top_rarest_badges`
),

-- Retrieve post answers
_posts AS (
    SELECT *
    FROM
        `deep-learning-438509.curated_stackoverflow_data_model.post_answers`
),

-- Define the column has_most_rare_badges
_users_badges AS (
    SELECT
        users.*,
        COALESCE(
            MAX(CASE WHEN badges.badge_name IS NOT NULL THEN 1 ELSE 0 END),
            0
        ) AS has_most_rare_badges
    FROM
        _users AS users
    LEFT JOIN UNNEST(users.badges_list) AS user_badge
    LEFT JOIN _badges AS badges
        ON user_badge = badges.badge_name
    -- Ensure to put together users with multiple badges
    GROUP BY ALL
),

-- Join with post answers
_users_with_post_answers AS (
    SELECT
        users.user_name,
        users.user_about_me,
        users.user_creation_date,
        users.user_location,
        users.user_reputation,
        users.user_up_votes,
        users.user_down_votes,
        users.user_views,
        users.user_profile_image_url,
        users.user_website_url,
        users.badge_count,
        users.badges_list,
        users.has_most_rare_badges,
        posts.answer_body,
        posts.answer_comment_count,
        posts.answer_creation_date,
        posts.answer_score
    FROM
        _users_badges AS users
    LEFT JOIN _posts AS posts
        ON _users_badges.user_id = posts.answer_user_id
)

-- Filter for users without post answers
SELECT
    *
FROM
    _users_with_post_answers
WHERE
    answer_body IS NOT NULL
