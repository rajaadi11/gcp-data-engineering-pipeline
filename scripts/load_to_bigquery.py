from google.cloud import bigquery
from pathlib import Path

# CONFIGURATION

PROJECT_ID = "fluted-lambda-507018-p8"
DATASET_ID = "sales_dataset"
TABLE_ID = "sales_table"

BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = BASE_DIR / "data" / "cleaned_sales_data.csv"

# CREATE BIGQUERY CLIENT

print("Connecting to BigQuery...")

client = bigquery.Client(project=PROJECT_ID)

print("Connected successfully.")

# DEFINE TABLE REFERENCE

table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

# DEFINE BIGQUERY SCHEMA

schema = [
    bigquery.SchemaField("order_id", "STRING"),
    bigquery.SchemaField("date", "DATE"),
    bigquery.SchemaField("region", "STRING"),
    bigquery.SchemaField("category", "STRING"),
    bigquery.SchemaField("product", "STRING"),
    bigquery.SchemaField("sales", "FLOAT"),
    bigquery.SchemaField("quantity", "INTEGER"),
    bigquery.SchemaField("discount", "FLOAT"),
    bigquery.SchemaField("profit", "FLOAT"),
]

# CONFIGURE LOAD JOB

job_config = bigquery.LoadJobConfig(
    schema=schema,
    skip_leading_rows=1,
    source_format=bigquery.SourceFormat.CSV,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
)

# LOAD CSV INTO BIGQUERY

print(f"Loading file: {CSV_FILE}")

with open(CSV_FILE, "rb") as source_file:

    load_job = client.load_table_from_file(
        source_file,
        table_ref,
        job_config=job_config,
    )

# WAIT FOR JOB TO COMPLETE

load_job.result()

# VERIFY TABLE

table = client.get_table(table_ref)

print()
print("=" * 50)
print("BIGQUERY LOAD COMPLETE")
print("=" * 50)

print(f"Table: {table_ref}")
print(f"Rows loaded: {table.num_rows}")
print(f"Columns: {len(table.schema)}")

print()
print("Schema:")

for field in table.schema:
    print(f"{field.name:<15} {field.field_type}")

print()
print("Pipeline completed successfully!")