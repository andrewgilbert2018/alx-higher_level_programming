-- a script the displays a list of same value in a record
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
