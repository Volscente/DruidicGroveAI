/*
 * Create a table including information from post answers for relevant users
 * Such users performed their last access between @last_access_starts_at and @last_access_ends_at.
 * They are retrieve from the time interval between @creation_date_start and @creation_date_end.
 * NOTE: The latest post answer's creation date is 25/09/2022 (Checked on 04/12/2024)
 * NOTE: 'owner_user_id' is the 'id' column of the user who posted the answer
 */
-- Retrieve relevant users IDs
WITH _users AS (
    SELECT users.id AS user_id
    FROM
        `bigquery-public-data.stackoverflow.users` AS users
    WHERE
        -- Filter for last access date
        users.last_access_date BETWEEN @last_access_starts_at AND @last_access_ends_at
        -- Filter for relevant information filled
        AND users.display_name IS NOT NULL
        AND users.location IS NOT NULL
),

-- Retrieve post answers for the relevant users
_post_aswers AS (
    SELECT
        posts_answers.owner_user_id AS answer_user_id,
        posts_answers.body AS answer_body,
        posts_answers.comment_count AS answer_comment_count,
        posts_answers.creation_date AS answer_creation_date,
        posts_answers.score AS answer_score
    FROM
        `bigquery-public-data.stackoverflow.posts_answers` AS posts_answers
    WHERE
        posts_answers.owner_user_id IN (SELECT users.user_id FROM _users AS users)
)

-- Filter for the specific time interval
SELECT *
FROM
    _post_aswers
WHERE
    answer_creation_date BETWEEN @creation_date_start AND @creation_date_end
