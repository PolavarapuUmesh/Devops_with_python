import os 
import shutil
import time
import datetime
dir_path='/home/umesh/Desktop/Terraform/providers/aws/dev/us-east-1/Terraform-providers-aws-dev-platform/ec2' #source file 
backup_path='/home/umesh/backup.txt'                                                                          #destination_path
while True:
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    backup_dir = os.path.join(backup_path, timestamp)
    os.makedirs(backup_dir)
    for file in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file)
        shutil.copy(file_path, backup_dir)
    print(f'Backup created at {timestamp}!')
    time.sleep(1000)  