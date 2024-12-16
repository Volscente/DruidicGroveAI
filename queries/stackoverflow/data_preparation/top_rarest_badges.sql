/*
 * Create a table including the @top_rarest_badges rarest gold badges between the
 * time interval @date_start and @date_end
 * and that at least @min_users_earned users earned it
 */
 -- TODO: Testing purpose - Remove afterward
-- Declare variables for the date range
DECLARE date_start TIMESTAMP;
DECLARE date_end TIMESTAMP;

-- Set values to the variables for testing purposes
SET date_start = TIMESTAMP("2013-01-01 00:00:00");
SET date_end = TIMESTAMP("2023-12-31 23:59:59");

-- Retrieve badges from the specified time interval
WITH _date_filtered_badges AS (
    SELECT
        badges.name
    FROM
        `bigquery-public-data.stackoverflow.badges` AS badges
    WHERE
        badges.date BETWEEN TIMESTAMP(date_start)
        AND TIMESTAMP(date_end)
        and badges.class = 1 -- Only gold badges
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
SELECT
  *
FROM
  _badges_rarity AS badges
WHERE
  badges.badge_rarity > @min_users_earned
LIMIT @top_rarest_badges

-- TODO: make parametrise to top_k and min_users -> change Query name, query docstring, eda, eda conclusions, documentation