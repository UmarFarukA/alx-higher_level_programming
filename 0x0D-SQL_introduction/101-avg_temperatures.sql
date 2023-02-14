-- Display Temparature in F
SELECT city, AVG(value) As avg_temp FROM temparatures GROUP By city ORDER By avg_temp DESC;
