from src.scraper import fetch_jobs
from src.utils.file_writer import save_to_csv
from src.report_generator import generate_summary_report
from src.utils.logger import logger

def main():
    logger.info("Starting job scraping workflow...")

    jobs = fetch_jobs()

    if not jobs:
        logger.warning("No jobs were scraped.")
        return

    save_to_csv(jobs)
    generate_summary_report("data/jobs.csv")

    logger.info("Job scraping workflow completed successfully.")

if __name__ == "__main__":
    main()