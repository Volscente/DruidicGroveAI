/*
 * Retrieve the number of badges obtained by each user in relevant users
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
        badges.date BETWEEN TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL 10 YEAR))
        AND TIMESTAMP(CURRENT_DATE())
),

-- Retrieve badge information of relevant users
_count_badges_relevant_users AS (
    SELECT
        users.id AS user_id,
        users.reputation AS user_reputation,
        users.up_votes AS user_up_votes,
        users.down_votes AS user_down_votes,
        users.views AS user_views,
        -- Compute the number of badges per user
        ROW_NUMBER() OVER (PARTITION BY users.id ORDER BY badges.date DESC) AS badge_count
    FROM
        _relevant_users AS users
    LEFT JOIN _badges AS badges
        ON users.id = badges.user_id
)

SELECT *
FROM _count_badges_relevant_users
