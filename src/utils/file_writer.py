import csv
from src.utils.logger import logger 

def save_to_csv(jobs, file_path="data/jobs.csv"):
    logger.info(f"Saving {len(jobs)} jobs to {file_path}...")

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Title", "Company", "Tags", "Link"])
            for job in jobs:
                writer.writerow([
                    job.get("title", ""),
                    job.get("company", ""),
                    ", ".join(job.get("tags", [])),
                    job.get("link", "")
                ])
        logger.info(f"✅ Jobs successfully saved to {file_path}")
    except Exception as e:
        logger.error(f"❌ Failed to save jobs to CSV: {e}")