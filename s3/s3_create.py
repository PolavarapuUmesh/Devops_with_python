import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3', region_name='us-east-1')

try:
    s3.create_bucket(Bucket='python-s3-bucket0001')
    print("Bucket created successfully.")
except ClientError as e:
    print(f"Error: {e}")

