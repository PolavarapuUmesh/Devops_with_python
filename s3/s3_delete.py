import boto3
from botocore.exceptions import ClientError

def delete_empty_bucket(bucket_name):
    s3 = boto3.client('s3')
    try:
        s3.head_bucket(Bucket=bucket_name)
    except ClientError as e:
        print(f"Error checking bucket existence: {e}")
        return
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' has been deleted.")
    except ClientError as e:
        print(f"Error deleting bucket: {e}")
if __name__ == "__main__":
    delete_empty_bucket('python-s3-bucket0001')
