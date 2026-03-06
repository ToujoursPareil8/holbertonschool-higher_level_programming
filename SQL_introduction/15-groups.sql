-- Lists the number of records with the same score
-- Result displays the score and the count (labeled as 'number')
-- Sorted by the count in descending order
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;