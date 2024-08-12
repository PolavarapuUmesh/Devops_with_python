import os
import subprocess

def setup_cron_job():
    # The cron job command
    cron_job = "48 3 * * * echo 1 | sudo tee /proc/sys/vm/drop_caches > /dev/null 2>&1"
    
    # Check existing cron jobs
    existing_crontab = subprocess.check_output(['crontab', '-l']).decode()

    # Check if the cron job already exists
    if cron_job not in existing_crontab:
        # Add the new cron job
        new_crontab = existing_crontab + cron_job + "\n"
        with subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE) as proc:
            proc.communicate(input=new_crontab.encode())
        print("Cron job added successfully!")
    else:
        print("Cron job already exists.")

if __name__ == "__main__":
    setup_cron_job()
