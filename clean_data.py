import pandas as pd
import re

# Load raw data
df = pd.read_csv("raw_data.csv")

# --- Clean phone numbers ---
def clean_phone(value):
    if pd.isna(value) or str(value).strip().lower() in ["n/a", ""]:
        return "Missing"
    digits = re.sub(r"[^0-9]", "", str(value))
    if len(digits) == 10:
        return f"{digits[0:3]}-{digits[3:6]}-{digits[6:10]}"
    return "Missing"

df["Phone_Number"] = df["Phone_Number"].apply(clean_phone)

# --- Clean names ---
def clean_name(value):
    if pd.isna(value):
        return "Missing"
    cleaned = re.sub(r"[^A-Za-z ]", "", str(value)).strip()
    return cleaned if cleaned else "Missing"

df["First_Name"] = df["First_Name"].apply(clean_name)
df["Last_Name"] = df["Last_Name"].apply(clean_name)

# --- Standardize Yes/No fields ---
def clean_yes_no(value):
    if pd.isna(value) or str(value).strip() == "":
        return "Unknown"
    return "Yes" if str(value).strip().upper().startswith("Y") else "No"

df["Paying_Customer"] = df["Paying Customer"].apply(clean_yes_no)
df = df.drop(columns=["Paying Customer"])
df["Do_Not_Contact"] = df["Do_Not_Contact"].apply(clean_yes_no) if "Do_Not_Contact" in df.columns else None

# --- Drop unnecessary column ---
if "Not_Useful_Column" in df.columns:
    df = df.drop(columns=["Not_Useful_Column"])

# --- Remove duplicate rows ---
df = df.drop_duplicates()

# --- Standardize missing addresses ---
df["Address"] = df["Address"].apply(lambda x: "Missing" if pd.isna(x) or str(x).strip().lower() == "n/a" else x)

# Save cleaned data
df = df[["CustomerID", "First_Name", "Last_Name", "Phone_Number", "Address", "Paying_Customer", "Do_Not_Contact"]]
df.to_csv("cleaned_data_python.csv", index=False)

print("Cleaning complete. Saved as cleaned_data_python.csv")
print(df.head(20))