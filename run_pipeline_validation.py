import sys
import shutil
import subprocess
import os

INPUT_PATH = "data/events_large.csv"
VALIDATED_PATH = "data/validated/events_large.csv"
REPORT_PATH = "report.xml"

def run_tests():
    print("running data validation results")
    result = subprocess.run(
        ["pytest", "tests/test_assert_python.py", f"--junitxml={REPORT_PATH}"],
        capture_output= True,
        text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print("failed")
        print(result.stderr)
        sys.exit(1)
    else:
        print("Passed")

def copy_validated_file():
    shutil.copyfile(INPUT_PATH, VALIDATED_PATH)
    print(f"file copied to {VALIDATED_PATH}")

if __name__ == "__main__":
    run_tests()
    copy_validated_file()


