/*
 * Create a table including information from relevant users
 */
-- CREATE OR REPLACE TABLE `deep-learning-438509.curated_stackoverflow_data_model.users_information` AS
-- Compute the latest access datetime
WITH _max_last_access_date AS (
    SELECT MAX(users.last_access_date) AS max_last_access_date
    FROM
        `bigquery-public-data.stackoverflow.users` AS users
),

-- Select only users for which the last access is maximum 8 hours greater than the max_last_access_date
_most_recent_last_access_users AS (
    SELECT users.*
    FROM
        `bigquery-public-data.stackoverflow.users` AS users,
        _max_last_access_date
    WHERE
        users.last_access_date BETWEEN TIMESTAMP(DATE_SUB(_max_last_access_date.max_last_access_date, INTERVAL ... HOUR))
        AND _max_last_access_date.max_last_access_date
)