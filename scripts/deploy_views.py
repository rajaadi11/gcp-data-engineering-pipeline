from pathlib import Path

from google.cloud import bigquery


PROJECT_ID = "fluted-lambda-507018-p8"

BASE_DIR = Path(__file__).resolve().parent.parent
VIEWS_DIR = BASE_DIR / "sql" / "views"


def deploy_views():
    print("Connecting to BigQuery...")

    client = bigquery.Client(project=PROJECT_ID)

    print("Connected successfully.")
    print()

    sql_files = sorted(VIEWS_DIR.glob("*.sql"))

    if not sql_files:
        raise FileNotFoundError(
            f"No SQL view files found in: {VIEWS_DIR}"
        )

    print(f"Views found: {len(sql_files)}")
    print()

    for sql_file in sql_files:

        print(f"Deploying: {sql_file.name}")

        query = sql_file.read_text(
            encoding="utf-8"
        )

        query_job = client.query(query)

        query_job.result()

        print(f"✅ Deployed: {sql_file.stem}")
        print()

    print("=" * 50)
    print("BIGQUERY VIEWS DEPLOYED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    deploy_views()