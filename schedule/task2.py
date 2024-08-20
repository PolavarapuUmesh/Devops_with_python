import time
import schedule

def backup():
    print("Every day backup at 7AM")
# schedule.every().monday.do(backup)
schedule.every().day.at("15:15").do(backup)
# schedule.every(1).hour.do(backup)
# schedule.every(1).minute.do(backup)
# schedule.every(10).seconds.do(backup)
while True:  # this loop keeps the script running continuosly
    schedule.run_pending()  # checks if a scheduled task is due to run and executes it
    time.sleep(1)  # Job runs at every 1 sec
    