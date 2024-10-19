-- Query for testing purposes
SELECT
    id,
    display_name
FROM
    `bigquery-public-data.stackoverflow.users`
WHERE
    id = @test_parameter