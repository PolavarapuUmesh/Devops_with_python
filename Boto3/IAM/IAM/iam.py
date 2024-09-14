import boto3

iam_client = boto3.client('iam')

def get_attached_policies(role_name):
    """Get the attached policies for the specified role."""
    response = iam_client.list_attached_role_policies(RoleName=role_name)
    return response['AttachedPolicies']

def create_new_role(new_role_name, assume_role_policy_document):
    """Create a new IAM role."""
    response = iam_client.create_role(
        RoleName=new_role_name,
        AssumeRolePolicyDocument=assume_role_policy_document
    )
    return response['Role']

def attach_policies_to_role(role_name, policies):
    """Attach the specified policies to the role."""
    for policy in policies:
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy['PolicyArn']
        )

def replicate_role_policies(old_role_name, new_role_name, assume_role_policy_document):
    """Replicate policies from the old role to the new role."""
    # Get the policies attached to the old role
    attached_policies = get_attached_policies(old_role_name)

    # Create the new role
    new_role = create_new_role(new_role_name, assume_role_policy_document)

    # Attach the same policies to the new role
    attach_policies_to_role(new_role_name, attached_policies)

    print(f"Successfully replicated policies from {old_role_name} to {new_role_name}")

if __name__ == "__main__":
    # Set the old and new role names
    old_role_name = 'test-fun-role-ay2ykm22 '
    new_role_name = 'user-001'
    
    # Define the assume role policy document (usually required when creating a role)
    assume_role_policy_document = '''{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }'''

    replicate_role_policies(old_role_name, new_role_name, assume_role_policy_document)
