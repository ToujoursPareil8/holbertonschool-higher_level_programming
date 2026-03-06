-- Lists all records with a name value, ordered by score (top first)
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;