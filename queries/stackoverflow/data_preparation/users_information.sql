/*
 * Create a table including information from relevant users
 * Such users performed their last access within the last @hours_interval hours
 * from the maximum last access datetime of all users.
 */
CREATE OR REPLACE TABLE `deep-learning-438509.curated_stackoverflow_data_model.users_information` AS

-- Compute the latest access datetime
WITH _max_last_access_date AS (
    SELECT MAX(users.last_access_date) AS max_last_access_date
    FROM
        `bigquery-public-data.stackoverflow.users` AS users
),

/*
 * Select only users for which the last access is maximum 8 hours greater than the max_last_access_date
 * and that have relevant information filled
*/
_most_recent_last_access_users AS (
    SELECT users.*
    FROM
        `bigquery-public-data.stackoverflow.users` AS users,
        _max_last_access_date
    WHERE
        -- Filter for last access date
        users.last_access_date BETWEEN TIMESTAMP(DATE_SUB(
            _max_last_access_date.max_last_access_date,
            INTERVAL @hours_interval HOUR
        ))
        AND _max_last_access_date.max_last_access_date
        -- Filter for relevant information filled
        AND users.display_name IS NOT NULL
        AND users.location IS NOT NULL
),

-- Retrieve badges information for the relevant users
_badges AS (
    SELECT
        badges.user_id AS badge_user_id,
        badges.name AS badge_name
    FROM
        `bigquery-public-data.stackoverflow.badges` AS badges
    WHERE
        badges.user_id IN (
            SELECT users.id
            FROM _most_recent_last_access_users AS users
        )
),

-- Aggregate badges into a single row per user
_badges_aggregated AS (
    SELECT
        badge_user_id,
        COUNT(badge_name) AS badge_count, -- Total badge occurrences, including duplicates
        ARRAY_AGG(DISTINCT badge_name) AS badges_list -- Distinct badge names in the list
    FROM
        _badges
    GROUP BY
        badge_user_id
)

-- Join users and badges information
SELECT
    users.id AS user_id,
    users.display_name AS user_name,
    users.about_me AS user_about_me,
    users.creation_date AS user_creation_date,
    users.location AS user_location,
    users.reputation AS user_reputation,
    users.up_votes AS user_up_votes,
    users.down_votes AS user_down_votes,
    users.views AS user_views,
    users.profile_image_url AS user_profile_image_url,
    users.website_url AS user_website_url,
    badges.badge_count,
    badges.badges_list
FROM
    _most_recent_last_access_users AS users
LEFT JOIN _badges_aggregated AS badges
    ON users.id = badges.badge_user_id
