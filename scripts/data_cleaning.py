import pandas as pd
from pathlib import Path

# 1. Define file paths

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "sales_data.csv"
OUTPUT_FILE = BASE_DIR / "data" / "cleaned_sales_data.csv"

# 2. Load raw data

print("Loading raw dataset...")

df = pd.read_csv(INPUT_FILE, encoding="cp1252")

print(f"Raw records: {len(df)}")

# 3. Select required columns

required_columns = [
    "Order ID",
    "Order Date",
    "Region",
    "Category",
    "Product Name",
    "Sales",
    "Quantity",
    "Discount",
    "Profit"
]

df = df[required_columns]

# 4. Rename columns using snake_case

df = df.rename(columns={
    "Order ID": "order_id",
    "Order Date": "date",
    "Region": "region",
    "Category": "category",
    "Product Name": "product",
    "Sales": "sales",
    "Quantity": "quantity",
    "Discount": "discount",
    "Profit": "profit"
})

# 5. Convert date column

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

# 6. Remove completely duplicated records

before_duplicates = len(df)

df = df.drop_duplicates()

duplicates_removed = before_duplicates - len(df)

# 7. Remove records with invalid critical fields

before_validation = len(df)

df = df.dropna(
    subset=[
        "order_id",
        "date",
        "region",
        "category",
        "product",
        "sales",
        "quantity"
    ]
)

invalid_records_removed = before_validation - len(df)

# 8. Validate numerical values

df = df[df["quantity"] > 0]

df = df[df["sales"] >= 0]

df = df[df["discount"].between(0, 1)]

# 9. Save cleaned dataset

df.to_csv(
    OUTPUT_FILE,
    index=False
)

# 10. Print pipeline summary

print("\nData cleaning completed successfully.")

print(f"Final records: {len(df)}")
print(f"Duplicates removed: {duplicates_removed}")
print(f"Invalid records removed: {invalid_records_removed}")

print("\nFinal schema:")
print(df.dtypes)

print(f"\nCleaned dataset saved to:")
print(OUTPUT_FILE)