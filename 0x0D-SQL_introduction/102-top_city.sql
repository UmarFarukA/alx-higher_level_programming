-- Display Temparature in F
SELECT city, AVG(value) As avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP By city ORDER By avg_temp DESC LIMIT 3;
