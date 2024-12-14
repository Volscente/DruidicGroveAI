/*
 * Create a table including the top 10 rarest badges between the
 * time interval @date_start and @date_end
 */
-- TODO: Testing purpose - Remove afterward
-- Declare variables for the date range
DECLARE date_start TIMESTAMP;
DECLARE date_end TIMESTAMP;

-- Set values to the variables for testing purposes
SET date_start = TIMESTAMP("2015-01-01 00:00:00");
SET date_end = TIMESTAMP("2023-12-31 23:59:59");

-- Retrieve badges from the specified time interval
WITH _date_filtered_badges AS (
    SELECT
        badges.name
    FROM
        `bigquery-public-data.stackoverflow.badges` AS badges
    WHERE
        badges.date BETWEEN TIMESTAMP(@date_start)
        AND TIMESTAMP(@date_end)
)
-- Compute the top 10 rarest badges
SELECT
    badges.name AS badge_name,
    COUNT(*) AS count
FROM
    _date_filtered_badges AS badges
GROUP BY
    badges.name
ORDER BY
    count ASC,  -- Rarest badges first
    badges.name ASC    -- Break ties alphabetically
LIMIT 100;
-- TODO: Change to "Top 100" -> Query name, query docstring, GitHub issue, documentation input table
-- TODO: Add Engineer feature "badges_encoded" -> EDA, EDA conclusion documentation, documentation training dataset, documentation data preparation