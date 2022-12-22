import requests
import matplotlib.pyplot as plt

today = requests.get("https://bonbast-api.deta.dev/latest").json()
yesterday = requests.get("https://bonbast-api.deta.dev/archive/").json()
#for i in range(5):
