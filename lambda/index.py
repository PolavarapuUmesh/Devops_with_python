import boto3
import pytz
import datetime
import time


s3=boto3.client('s3')
response=s3.list_buckets()
buckets = [bucket['Name'] for bucket in response['Buckets']]
print(buckets)                                                       #list of the buckets    
time_zone_name = time.tzname[time.daylight]
time_zone_offset = datetime.datetime.now(datetime.timezone.utc).astimezone().utcoffset()
print(f"Current time zone: {time_zone_name}")
print(f"Current UTC offset: {time_zone_offset}")
