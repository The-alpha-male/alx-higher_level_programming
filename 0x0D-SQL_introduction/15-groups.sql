-- lists the number of records with the same score from second_table
-- results display the score, number of records

SELECT score, COUNT(*)
as number FROM second_table
GROUP BY score ORDER BY number DESC;
