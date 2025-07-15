import csv
import os
from collections import Counter
from src.utils.logger import logger

def generate_summary_report(csv_file_path, output_path="reports/summary_report.txt"):
    logger.info("Generating summary report...")
    jobs = []

    try:
        with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            # Normalize headers to lowercase for flexible access
            lowercase_fieldnames = [field.lower() for field in reader.fieldnames]
            for row in reader:
                normalized_row = {
                    key.lower(): value for key, value in row.items()
                }

                title = normalized_row.get("title", "").strip()
                company = normalized_row.get("company", "").strip()
                tags = normalized_row.get("tags", "").strip()

                if title and company:
                    jobs.append({
                        "title": title,
                        "company": company,
                        "tags": tags
                    })

    except Exception as e:
        logger.error(f"Failed to read CSV: {e}")
        return

    total_jobs = len(jobs)
    logger.info(f"Total valid jobs: {total_jobs}")

    company_counter = Counter(job["company"] for job in jobs)
    tag_counter = Counter(
        tag.lower()
        for job in jobs
        for tag in job["tags"].strip("[]").replace("'", "").split(", ")
        if tag
    )

    top_companies = company_counter.most_common(5)
    top_tags = tag_counter.most_common(5)

    report = []
    report.append(f"📊 Total jobs scraped: {total_jobs}\n")
    report.append("🏢 Top Hiring Companies:")
    for company, count in top_companies:
        report.append(f"- {company}: {count} job(s)")

    report.append("\n🏷️ Most In-Demand Tags:")
    for tag, count in top_tags:
        report.append(f"- {tag}: {count} job(s)")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(report))
        logger.info(f"Summary report saved to {output_path}")
    except Exception as e:
        logger.error(f"Failed to save summary report: {e}")