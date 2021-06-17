import requests
res = requests.get('https://api.ipify.org/')
print(res.text)