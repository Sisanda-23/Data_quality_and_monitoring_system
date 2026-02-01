-- Check duplicates
SELECT transaction_id, COUNT(*)
FROM sales
GROUP BY transaction_id
HAVING COUNT(*) > 1;

-- Check missing sales
SELECT COUNT(*) 
FROM sales
WHERE sale_amount IS NULL;

-- Outlier check
SELECT *
FROM sales
WHERE sale_amount > 1000;

