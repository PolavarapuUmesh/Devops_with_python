# import boto3
# ec2 = boto3.client('ec2')
# response = ec2.start_instances(InstanceIds=['i-0417a7077b275bf80'])
# print("response")

import boto3
ec2 = boto3.client('ec2')
response = ec2.stop_instances(InstanceIds=['i-0417a7077b275bf80'])
print("response")