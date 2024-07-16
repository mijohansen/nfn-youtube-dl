from dotenv import load_dotenv

from notefornote import perform_download_task

load_dotenv()
result = perform_download_task()

print(result)
