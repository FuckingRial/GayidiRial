import requests
#import matplotlib.pyplot as plt

today = requests.get("https://bonbast-api.deta.dev/latest").json()
yesterday = requests.get("https://bonbast-api.deta.dev/archive/").json()
days = []
days.append(today)
days.append(yesterday)
d = yesterday["date"].split("-")
for i in range(5):
  days.append(requests.get("https://bonbast-api.deta.dev/archive/"+d[0]+"-"+d[1]+str(int(d[2])-i-1)).json())
print(days)
  
