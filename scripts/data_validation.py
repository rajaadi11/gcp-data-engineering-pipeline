import pandas as pd
from pathlib import Path

# 1. Define project paths

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "cleaned_sales_data.csv"

# 2. Load cleaned dataset

print("Loading cleaned dataset...")

df = pd.read_csv(INPUT_FILE, encoding="latin1")

print(f"Records loaded: {len(df)}")

# 3. Define expected schema

expected_columns = [
    "order_id",
    "date",
    "region",
    "category",
    "product",
    "sales",
    "quantity",
    "discount",
    "profit"
]

# 4. Validate columns

print("\nChecking schema...")

actual_columns = df.columns.tolist()

if actual_columns == expected_columns:
    print("PASS: Column schema is correct.")
else:
    print("FAIL: Column schema does not match.")
    print("Expected:", expected_columns)
    print("Actual:", actual_columns)

# 5. Check missing values

print("\nChecking missing values...")

missing_values = df[expected_columns].isnull().sum()

total_missing = missing_values.sum()

if total_missing == 0:
    print("PASS: No missing values found.")
else:
    print("FAIL: Missing values found.")
    print(missing_values[missing_values > 0])

# 6. Check duplicate records

print("\nChecking duplicate records...")

duplicates = df.duplicated().sum()

if duplicates == 0:
    print("PASS: No duplicate records found.")
else:
    print(f"FAIL: {duplicates} duplicate records found.")

# 7. Validate quantity

print("\nChecking quantity values...")

invalid_quantity = (df["quantity"] <= 0).sum()

if invalid_quantity == 0:
    print("PASS: All quantity values are valid.")
else:
    print(f"FAIL: {invalid_quantity} invalid quantity values found.")

# 8. Validate sales

print("\nChecking sales values...")

invalid_sales = (df["sales"] < 0).sum()

if invalid_sales == 0:
    print("PASS: All sales values are valid.")
else:
    print(f"FAIL: {invalid_sales} invalid sales values found.")

# 9. Validate discount

print("\nChecking discount values...")

invalid_discount = (
    (~df["discount"].between(0, 1))
).sum()

if invalid_discount == 0:
    print("PASS: All discount values are valid.")
else:
    print(f"FAIL: {invalid_discount} invalid discount values found.")

# 10. Final summary

print("\n" + "=" * 50)
print("DATA QUALITY VALIDATION COMPLETE")
print("=" * 50)

print(f"Total records: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"Total missing values: {total_missing}")
print(f"Total duplicates: {duplicates}")
print(f"Invalid quantities: {invalid_quantity}")
print(f"Invalid sales: {invalid_sales}")
print(f"Invalid discounts: {invalid_discount}")