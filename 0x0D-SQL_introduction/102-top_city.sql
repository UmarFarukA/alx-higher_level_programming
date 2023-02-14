-- Display Temparature in F
SELECT city, AVG(value) As avg_temp FROM temperatures GROUP By city ORDER By avg_temp DESC LIMIT 3;
