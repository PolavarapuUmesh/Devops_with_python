import boto3
import json

ec2 = boto3.client('ec2')
sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        response = ec2.create_snapshot(
            VolumeId='vol-05251a525b9351ff6', 
            Description='Daily snapshot'
        )
        
        snapshot_id = response['SnapshotId']
        
        message = f'Snapshot created: {snapshot_id}'
        
        sns.publish(
            TopicArn='arn:aws:sns:us-east-1:471112674723:SnapshotNotificationTopic:9f0ef47d-4d7f-4fa1-974f-c7e2e547fce0', 
            Subject='Snapshot Creation Notification',
            Message=message
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps({'message': message})
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }