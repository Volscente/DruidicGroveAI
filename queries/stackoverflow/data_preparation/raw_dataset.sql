/*
 * Create a table by joining the following input tables for the StackOverflow use case:
 * 1. `deep-learning-438509.curated_stackoverflow_data_model.users_information`
 * 2. `deep-learning-438509.curated_stackoverflow_data_model.top_rarest_badges`
 * 3. `deep-learning-438509.curated_stackoverflow_data_model.post_answers`
 */

-- Retrieve users information
WITH _users AS (
    SELECT *
    FROM
        `deep-learning-438509.curated_stackoverflow_data_model.users_information`
),

-- Retrieve top rarest badges
_badges AS (
    SELECT *
    FROM
        `deep-learning-438509.curated_stackoverflow_data_model.top_rarest_badges`
),

-- Retrieve post answers
_posts AS (
    SELECT *
    FROM
        `deep-learning-438509.curated_stackoverflow_data_model.post_answers`
)