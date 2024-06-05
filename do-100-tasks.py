from notefornote import do_complete_task

for i in range(10000):
    try:
        print(do_complete_task())
    except Exception as inst:
        print(inst)

print("Jobs done.")
