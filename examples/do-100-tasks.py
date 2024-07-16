from dotenv import load_dotenv

from notefornote import perform_download_task

load_dotenv()

for i in range(10000):
    try:
        print(perform_download_task())
    except Exception as inst:
        print(inst)

print("Jobs done.")
