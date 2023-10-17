-- Step 1: Import the table dump (assuming the file is named 'table_dump.sql')
-- USE hbtn_0c_0;
SOURCE /var/lib/mysql/temperatures.sql;

 
-- Step 2: Calculate the average temperature by city and order by temperature (descending)
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
