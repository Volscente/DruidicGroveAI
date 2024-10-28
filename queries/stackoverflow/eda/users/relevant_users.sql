/*
 * Retrieve all the users that have not null values in their information
 * from the ones who recently performed their last access into the platform
*/
WITH _max_last_access_date AS (
  SELECT
    MAX(user.last_access_date) AS max_last_access_date
  FROM
    `bigquery-public-data.stackoverflow.users` AS user
),
_most_recent_last_access_users AS (
  SELECT
    *
FROM
  `bigquery-public-data.stackoverflow.users` AS user,
  _max_last_access_date
WHERE
  user.last_access_date BETWEEN TIMESTAMP(DATE_SUB(_max_last_access_date.max_last_access_date, INTERVAL 8 HOUR))
  AND _max_last_access_date.max_last_access_date
)
# TODO
# Add filters for users with all information filled