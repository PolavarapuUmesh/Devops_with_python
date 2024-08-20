import requests

response = requests.get('https://www.vignan.ac.in')
html = response.text
print(html)
