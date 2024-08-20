import schedule
import time

def job():
    print("Job is running at 11 AM")

# Schedule the job to run every day at 6 AM
schedule.every(1).day.at("11:00").do(job)

try:
    while True:
        # Run all scheduled jobs
        schedule.run_pending()
        # Sleep for a short time before checking again
        time.sleep(60)
except KeyboardInterrupt:
    print("Interrupted by user. Exiting...")
    # Perform any cleanup tasks here if necessary
