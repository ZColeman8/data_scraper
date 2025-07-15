import os
import pytest
from src.scraper import fetch_jobs
from src.utils.file_writer import save_to_csv
from src.utils.logger import logger  

def test_fetch_jobs_returns_data():
    """Test that fetch_jobs returns a non-empty list with expected keys."""
    logger.info("Running fetch_jobs test...")
    jobs = fetch_jobs()
    assert isinstance(jobs, list), "Expected a list of jobs"
    assert len(jobs) > 0, "Expected at least one job result"
    logger.info(f"✔️ Retrieved {len(jobs)} job listings.")

    required_keys = {"title", "company", "tags", "link"}
    for job in jobs:
        assert required_keys.issubset(job.keys()), f"Missing keys in job: {job}"


def test_save_jobs_creates_valid_csv(tmp_path):
    """Test saving jobs to CSV and verifying file content."""
    logger.info("Running CSV export test...")
    jobs = fetch_jobs()
    test_file = tmp_path / "test_jobs.csv"
    save_to_csv(jobs, file_path=str(test_file))

    assert os.path.exists(test_file), "CSV file was not created"
    logger.info(f"✔️ CSV file created: {test_file}")

    with open(test_file, encoding="utf-8") as f:
        content = f.read()
        assert "title" in content.lower(), "CSV file is missing expected headers"
    logger.info("✔️ CSV file contains expected content.")
