# Data Dictionary

## dim_fund

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | AMFI Scheme Code |
| fund_house | TEXT | Mutual Fund House |
| scheme_name | TEXT | Scheme Name |
| category | TEXT | Fund Category |
| sub_category | TEXT | Fund Sub Category |
| plan | TEXT | Direct / Regular |
| expense_ratio_pct | REAL | Expense Ratio |
| risk_category | TEXT | Risk Classification |

---

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

---

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor Identifier |
| transaction_date | DATE | Transaction Date |
| amount_inr | INTEGER | Amount Invested |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |

---

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| return_1yr_pct | REAL | 1 Year Return |
| return_3yr_pct | REAL | 3 Year Return |
| return_5yr_pct | REAL | 5 Year Return |
| sharpe_ratio | REAL | Risk Adjusted Return |
| alpha | REAL | Excess Return |
| beta | REAL | Market Sensitivity |