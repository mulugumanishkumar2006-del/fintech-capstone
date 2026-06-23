-- 1. Top 5 fund houses by AUM

SELECT fund_house,
       MAX(aum_crore) AS max_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY max_aum DESC
LIMIT 5;


-- 2. Average NAV per fund

SELECT amfi_code,
       ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;


-- 3. Total transactions by state

SELECT state,
       SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;


-- 4. Transaction count by type

SELECT transaction_type,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;


-- 5. Funds with expense ratio below 1%

SELECT scheme_name,
       expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;


-- 6. Top 10 funds by 3-year return

SELECT scheme_name,
       return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;


-- 7. Average Sharpe Ratio

SELECT ROUND(AVG(sharpe_ratio),2)
AS avg_sharpe
FROM fact_performance;


-- 8. Total SIP inflow

SELECT SUM(sip_inflow_crore)
AS total_sip_inflow
FROM fact_sip_industry;


-- 9. Number of schemes by category

SELECT category,
       COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY category;


-- 10. Top performing funds by Alpha

SELECT amfi_code,
       alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;