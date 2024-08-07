import boto3
from botocore.exceptions import ClientError
def upload_file_to_bucket(file_name, bucket_name, object_name=None):
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = file_name
    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"File '{file_name}' uploaded to bucket '{bucket_name}' as '{object_name}'.")
    except ClientError as e:
        print(f"Error uploading file: {e}")
if __name__ == "__main__":
    file_name = '/home/umesh/user.html' 
    bucket_name = 'python-s3-bucket0001' 
    object_name = 'user.html'            
    upload_file_to_bucket(file_name, bucket_name, object_name)
