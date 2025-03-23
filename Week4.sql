SELECT 
	count(DISTINCT s.Order_id) 
FROM SALES s JOIN CUSTOMERS c
ON s.Customer_id = c.Customer_id
WHERE s.Date = '2023-03-18' 
AND c.first_name = 'John' AND c.last_name = 'Doe';

SELECT 
    COUNT(*) AS Total_Customers,
    AVG(TotalSpent) AS Avg_Spent_Per_Customer
FROM (
    SELECT Customer_id, SUM(Revenue) AS TotalSpent
    FROM SALES
    WHERE Date >= '2023-01-01' AND Date < '2023-02-01'
    GROUP BY Customer_id
) AS CustomerSales;

SELECT i.department
FROM SALES s
JOIN ITEMS i ON s.Item_id = i.Item_id
WHERE s.Date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY i.department
HAVING SUM(s.Revenue) < 600;

SELECT 
    MAX(OrderTotal) AS Most_Revenue, 
    MIN(OrderTotal) AS Least_Revenue
FROM (
    SELECT Order_id, SUM(Revenue) AS OrderTotal
    FROM SALES
    GROUP BY Order_id
) AS OrderRevenue;

WITH max_order as (
	SELECT Order_id
    FROM SALES
    GROUP BY Order_id
    ORDER BY SUM(Revenue) DESC
    LIMIT 1
)
SELECT s.Order_id
FROM SALES s
JOIN max_order m ON s.Order_id = m.Order_id;
