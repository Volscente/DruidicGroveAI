/*
 * Retrieve badge information of the relevant users
*/
-- Retrieve relevant users
WITH _relevant_users AS (
    SELECT *
    FROM
        `deep-learning-438509.dim_stackoverflow_data_model.relevant_users`
),

-- Retrieve badge information
_badges AS (
    SELECT *
    FROM
        `bigquery-public-data.stackoverflow.badges`
),

-- Retrieve badge information of relevant users
_badges_relevant_users AS (
    SELECT
    FROM
        _badges as badges
    
)

