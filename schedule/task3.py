import schedule
import time
def job():
    print("Runs daily at 7AM")
schedule.every().day.at("7:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(5)