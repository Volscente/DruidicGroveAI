/*
 * Create a table including information from relevant users
 * Such users performed their last access within the last @hours_interval hours
 * from the maximum last access datetime of all users.
 */
-- TODO: Remove after testing
-- CREATE OR REPLACE TABLE `deep-learning-438509.curated_stackoverflow_data_model.users_information` AS
-- TODO: Testing purpose - Remove afterward
-- Declare variables for the date range
DECLARE hours_interval INT64;

-- Set values to the variables for testing purposes
SET hours_interval = 8;

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
                INTERVAL hours_interval HOUR))
        AND _max_last_access_date.max_last_access_date
        -- Filter for relevant information filled
        AND users.display_name IS NOT NULL
        AND users.location IS NOT NULL
),

-- Retrieve badges information for the relevant users
_badges AS (
    SELECT
        badges.user_id AS badge_user_id,
        badges.name AS badge_name,
    FROM
        `bigquery-public-data.stackoverflow.badges` AS badges
    WHERE
        badges.user_id IN (
            SELECT users.id
            FROM _most_recent_last_access_users AS users
        )
)

SELECT
    COUNT(*)
FROM
    _badges

