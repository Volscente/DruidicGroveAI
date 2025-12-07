/*
 * Test query for checking the function
 * stackoverflow/data_preparation/data_preparation
 * .AnswerScoreDataPreparator.download_raw_data function.
 */
SELECT users.display_name
FROM
    `bigquery-public-data.stackoverflow.users` AS users
LIMIT 1