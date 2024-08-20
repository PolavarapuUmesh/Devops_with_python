import schedule
import time
def job():
    print("Daily this job runs at 7AM")
schedule.every(1).day.at("07:00 ").do(job)
while True:
    schedule.run_pending()
    time.sleep(5)