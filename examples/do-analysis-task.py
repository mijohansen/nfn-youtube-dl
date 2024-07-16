from dotenv import load_dotenv

from notefornote import perform_analysis_task

load_dotenv()
result = perform_analysis_task()

print(result)
