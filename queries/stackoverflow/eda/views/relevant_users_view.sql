/*
 * Retrieve all the users that have not null values in their information
 * from the ones who recently performed their last access into the platform
*/
CREATE OR REPLACE TABLE `deep-learning-438509.dim_stackoverflow_data_model.relevant_users` AS
-- Compute the latest access datetime
WITH _max_last_access_date AS (
    SELECT MAX(stackoverflow_user.last_access_date) AS max_last_access_date
    FROM
        `bigquery-public-data.stackoverflow.users` AS stackoverflow_user
),

-- Select only users for which the last access is maximum 8 hours greater than the max_last_access_date
_most_recent_last_access_users AS (
    SELECT stackoverflow_user.*
    FROM
        `bigquery-public-data.stackoverflow.users` AS stackoverflow_user,
        _max_last_access_date
    WHERE
        stackoverflow_user.last_access_date BETWEEN TIMESTAMP(DATE_SUB(_max_last_access_date.max_last_access_date, INTERVAL 8 HOUR))
        AND _max_last_access_date.max_last_access_date
)

-- Select only users which have all the information filled
-- NOTE: age is rarely filled
SELECT relevant_user.*
FROM
    _most_recent_last_access_users AS relevant_user
WHERE
    relevant_user.display_name IS NOT NULL
    AND relevant_user.location IS NOT NULL