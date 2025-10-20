## Bonus Feature: Smarter Job CSV (Filtering, De-dup, Sorting)
- Added `scrape_fake_jobs_to_csv_filtered()`:
  - Filter by keyword in job title (default: “Python”)
  - Filter out old postings via `min_date` (YYYY-MM-DD)
  - Remove duplicate listings (same title/company/location/date)
  - Sort newest-to-oldest by date
  - Exports to **fake_jobs_filtered.csv**


