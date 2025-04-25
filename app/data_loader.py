import pandas as pd
import json

def fetch_relevant_info(query: str) -> str:
    info = ""

    # Load job data
    try:
        df_jobs = pd.read_csv("data/job_listing_data.csv")
        relevant_jobs = df_jobs[df_jobs["title"].str.contains(query, case=False, na=False)]
        info += "Job Listings:\n" + "\n".join(relevant_jobs["title"].head(3)) + "\n"
    except:
        info += "Job data not available.\n"

    # Load session details
    try:
        with open("data/session_details.json") as f:
            sessions = json.load(f)
            matched = [s for s in sessions if query.lower() in s["title"].lower()]
            if matched:
                info += "Sessions:\n" + "\n".join(s["title"] for s in matched[:3]) + "\n"
    except:
        info += "Session data not available.\n"

    return info
