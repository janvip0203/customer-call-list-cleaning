# Customer Call List – Data Cleaning Project

## Overview
This project takes a raw, messy customer contact list and cleans it into a consistent, analysis-ready dataset using Google Sheets formulas (REGEXREPLACE, REGEXMATCH, TRIM, TEXT).

## Files
- `raw_data.csv` – original, messy dataset
- `cleaned_data.csv` – cleaned, standardized dataset

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
Google Sheets — REGEXREPLACE, REGEXMATCH, TRIM, TEXT functions
