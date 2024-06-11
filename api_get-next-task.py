from dotenv import load_dotenv

from notefornote import create_analysis_task

load_dotenv()
next_task = create_analysis_task()

print(next_task)
print(next_task["platform_ident"])
