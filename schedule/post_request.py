import requests
url="https://www.vignan.ac.in"
data={
    'user':'nimmesh',    
    'email':'nimmeshprasad2@gmail.com'
}
response=requests.post(url,json=data)
if response.status_code==200:
    print('request was successful')
else:
    print('request failed with status code:',response.status_code)

