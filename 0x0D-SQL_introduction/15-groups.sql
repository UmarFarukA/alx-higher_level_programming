-- Display the number score that are same score
SELECT score, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
