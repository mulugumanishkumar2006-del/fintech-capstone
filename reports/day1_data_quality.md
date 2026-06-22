# Day 1: Data Ingestion & Quality Report

## Project Overview

The objective of Day 1 was to set up the project environment, ingest the provided datasets, perform initial data validation, and fetch live mutual fund NAV data from the MFAPI.

---

## Tasks Completed

* Created the project folder structure.
* Initialized a Git repository.
* Installed all required Python dependencies.
* Generated `requirements.txt`.
* Loaded all 10 CSV datasets using Pandas.
* Examined each dataset using `.shape`, `.dtypes`, and `.head()`.
* Performed basic data quality checks.
* Retrieved live NAV data using the MFAPI.
* Prepared scripts for fund master exploration and AMFI code validation.

---

## Dataset Summary

| Dataset               |   Rows | Columns | Status               |
| --------------------- | -----: | ------: | -------------------- |
| Fund Master           |     40 |      15 | Clean                |
| NAV History           | 46,000 |       3 | Clean                |
| AUM by Fund House     |     90 |       5 | Clean                |
| Monthly SIP Inflows   |     48 |       6 | Minor missing values |
| Category Inflows      |    144 |       3 | Clean                |
| Industry Folio Count  |     21 |       6 | Clean                |
| Scheme Performance    |     40 |      19 | Clean                |
| Investor Transactions | 32,778 |      13 | Clean                |
| Portfolio Holdings    |    322 |       8 | Clean                |
| Benchmark Indices     |  8,050 |       3 | Clean                |

---

## Data Quality Findings

### Missing Values

* No missing values were found in 9 out of the 10 datasets.
* The `yoy_growth_pct` column in the Monthly SIP Inflows dataset contains 12 missing values. These are expected because Year-over-Year growth cannot be calculated for the first year of data.

### Duplicate Records

* No duplicate rows were detected in any dataset.

### Data Types

* Numeric columns were correctly identified as `int64` or `float64`.
* Date columns are currently stored as strings (`object`) and should be converted to `datetime` during preprocessing.

### AMFI Scheme Codes

* AMFI scheme codes were successfully loaded from the fund master dataset.
* Validation against the NAV history dataset was completed to ensure data consistency.

---

## Live NAV Fetch

Successfully connected to the MFAPI and downloaded the latest available NAV history for the specified mutual fund scheme.

---

## Conclusion

Day 1 objectives were successfully completed. The project environment is fully configured, datasets have been ingested, initial quality checks have been performed, and the data is ready for preprocessing and exploratory analysis in the next phase.
