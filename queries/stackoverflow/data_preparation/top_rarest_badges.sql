/*
 * Create a table including the @top_rarest_badges rarest gold badges between the
 * time interval @date_start and @date_end
 * and that at least @min_users_earned users earned it
 */
CREATE OR REPLACE TABLE `deep-learning-438509.curated_stackoverflow_data_model.top_rarest_badges` AS
-- Retrieve badges from the specified time interval
WITH _date_filtered_badges AS (
    SELECT badges.name
    FROM
        `bigquery-public-data.stackoverflow.badges` AS badges
    WHERE
        badges.date BETWEEN TIMESTAMP(@date_start)
        AND TIMESTAMP(@date_end)
        AND badges.class = 1 -- Only gold badges
),

-- Compute the rarity of the badges
_badges_rarity AS (
    SELECT
        badges.name AS badge_name,
        COUNT(*) AS badge_rarity
    FROM
        _date_filtered_badges AS badges
    GROUP BY
        badges.name
    ORDER BY
        badge_rarity
)

-- Select top  most rare badges earned by at least a certain number of users
SELECT *
FROM
    _badges_rarity AS badges
WHERE
    badges.badge_rarity > @min_users_earned
LIMIT @top_rarest_badges
