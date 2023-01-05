import requests
from datetime import datetime as date
import matplotlib.pyplot as plt
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import os
try:
  os.remove("weekplot.png")
except:
  1
weekdays_cte = ["دوشنبه","سه شنبه","چهارشنبه","پنج شنبه","جمعه","شنبه","یکشنبه"]

today = requests.get("https://bonbast-api.deta.dev/latest").json()
yesterday = requests.get("https://bonbast-api.deta.dev/archive/").json()
days = []
days.append(today)
days.append(yesterday)
d = yesterday["date"].split("-")
for i in range(5):
  print(str(d[0]+"-"+d[1]+"-"+str(int(d[2])-i-1)))
  days.append(requests.get("https://bonbast-api.deta.dev/archive?date="+d[0]+"-"+d[1]+"-"+str(int(d[2])-i-1)).json())
print(days)
  
usd = []
weekdays = []
weekdays.append(weekdays_cte[date.today().weekday()])
usd.append(days[0]["usd"]["sell"])
for i in range(6):
  dd = days[i+1]["date"].split("-")
  weekdays.append(weekdays_cte[date(int(dd[0]),int(dd[1]),int(dd[2])).weekday()])
  usd.append(days[i+1]["usd"]["sell"])
print(weekdays)
print(usd)
persian_weekdays = [get_display(reshape(label)) for label in weekdays]
plt.plot(persian_weekdays, usd)
  
# naming the x axis
plt.ylabel(get_display(reshape('قیمت دلار')))
# naming the y axis
plt.xlabel(get_display(reshape('روز هفته')))
  
# giving a title to my graph
plt.title(get_display(reshape('پروژه گاییدن ریال')))
plt.gca().invert_xaxis()

# function to show the plot
plt.savefig('weekplot.png')
