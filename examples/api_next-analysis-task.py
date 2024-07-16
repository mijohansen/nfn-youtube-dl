from dotenv import load_dotenv

from notefornote import fetch_analysis_task

load_dotenv()
next_task = fetch_analysis_task()

print(next_task)
