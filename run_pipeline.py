import subprocess
import sys


def run_step(step_name, command):
    print()
    print("=" * 60)
    print(f"STARTING: {step_name}")
    print("=" * 60)

    result = subprocess.run(command)

    if result.returncode != 0:
        print()
        print(f"❌ FAILED: {step_name}")
        print("Pipeline stopped.")
        sys.exit(result.returncode)

    print()
    print(f"✅ COMPLETED: {step_name}")


def main():

    print()
    print("=" * 60)
    print("GCP DATA ENGINEERING PIPELINE")
    print("=" * 60)

    # Step 1: Clean raw data
    run_step(
        "DATA CLEANING",
        [sys.executable, "scripts/data_cleaning.py"]
    )

    # Step 2: Validate cleaned data
    run_step(
        "DATA VALIDATION",
        [sys.executable, "scripts/data_validation.py"]
    )

    # Step 3: Load data into BigQuery
    run_step(
        "BIGQUERY LOAD",
        [sys.executable, "scripts/load_to_bigquery.py"]
    )

    print()
    print("=" * 60)
    print("🎉 PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()