from dotenv import load_dotenv

from notefornote import fetch_download_task

load_dotenv()
next_task = fetch_download_task()

print(next_task)
