# import boto3

# ce = boto3.client('ce')

# response = ce.get_cost_and_usage(
#     TimePeriod={
#         'Start': '2024-08-01',
#         'End': '2024-08-30'
#     },
#     Granularity='MONTHLY',
#     Metrics=['BlendedCost']
# )
# for result in response['ResultsByTime']:
#     print("Time Period:", result['TimePeriod'])
#     print("Blended Cost:", result['Total']['BlendedCost']['Amount'])
#     print("Unit:", result['Total']['BlendedCost']['Unit'])

#Aug cost and usage 785 INR
#JULY cost and usage 972 INR
#JUNE  cost and usage 84 INR
import boto3
ce = boto3.client('ce')
response = ce.get_cost_and_usage(
    TimePeriod={
        'Start': '2024-08-01',
        'End': '2024-08-30'
    },
    Granularity='MONTHLY',
    Metrics=['BlendedCost']
)
usd_to_inr = 83.0
for result in response['ResultsByTime']:
    usd_cost = float(result['Total']['BlendedCost']['Amount'])
    inr_cost = usd_cost * usd_to_inr
    print("Time Period:", result['TimePeriod'])
    print(f"Blended Cost in USD: {usd_cost:.2f} USD")  
    print(f"Blended Cost in INR: {inr_cost:.2f} INR")
    
