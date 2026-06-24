# Customer Call List – Data Cleaning Project

## Overview
This project takes a raw, messy customer contact list and cleans it into a consistent, analysis-ready dataset using Google Sheets formulas (REGEXREPLACE, REGEXMATCH, TRIM, TEXT).

## Files
- `raw_data.csv` – original, messy dataset
- `cleaned_data.csv` – cleaned dataset (Google Sheets version)
- `clean_data.py` – Python script replicating the same cleaning logic using pandas
- `cleaned_data_python.csv` – cleaned dataset (Python version)

## Issues Identified in Raw Data
- Phone numbers in four different formats (dashes, slashes, pipes, plain digits)
- Extra whitespace in first/last names
- Junk characters embedded in last names (stray symbols, underscores)
- Inconsistent Yes/No values across two columns (`Y`, `N`, `Yes`, `No`, blank)
- One fully duplicated row
- One column with no analytical value
- Missing data inconsistently represented (blank cells vs. "N/a" text)

## Cleaning Steps Applied
1. Standardized all valid phone numbers to `XXX-XXX-XXXX` format using REGEXREPLACE + TEXT formatting
2. Removed extra whitespace from names using TRIM
3. Stripped non-letter characters from last names using REGEXREPLACE
4. Standardized Yes/No fields using REGEXMATCH logic, with genuinely blank values marked "Unknown" rather than guessed
5. Removed one exact duplicate row
6. Deleted a column with no analytical use
7. Standardized all missing values (blank, "N/a") to a single consistent "Missing" label

## Design Decision
The Address column was not split into separate City/State fields, since formatting was inconsistent across rows and doing so would have required inferring data that wasn't reliably present. This was a deliberate choice to avoid fabricating information.

## Tools Used
- Google Sheets — REGEXREPLACE, REGEXMATCH, TRIM, TEXT functions
- Python — pandas, re (regular expressions)

## Note
This project was completed twice using two different approaches — once in Google Sheets 
(formulas) and once in Python (pandas) — to demonstrate the same data cleaning logic 
applied with both spreadsheet tools and code.
