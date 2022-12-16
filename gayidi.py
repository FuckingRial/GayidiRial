import tweepy,json,os


consumer_key = os.environ.get("CK")
consumer_secret = os.environ.get("CS")
access_token = os.environ.get("AT")
access_token_secret = os.environ.get("ATS")

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# Create Tweet

# The app and the corresponding credentials must have the Write permission

# Check the App permissions section of the Settings tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps

# Make sure to reauthorize your app / regenerate your access token and secret 
# after setting the Write permission

with open('gayidirial') as f:
    emruz = json.load(f)
    print(emruz)
    
with open('gayidirialdiruz') as f:
    print(str(f))
    diruz = json.load(f)
    print(diruz)
    
with open('btc') as f:
    btc = json.load(f)
    print(btc)
text = "دلار: " + str(emruz["usd"]["sell"]) + "\n بیتکوین: " +str(btc["stats"]["btc-rls"]["dayClose"]) + "\n بیتکوین-دلار: " + str(btc["global"]["binance"]["btc"])
if emruz["usd"]["sell"] > diruz["usd"]["sell"]:
    text = text + "\n امروز" +str(round(100*(emruz["usd"]["sell"] - diruz["usd"]["sell"])/ diruz["usd"]["sell"]),2) + " درصد فقیر تر شدیم "
response = client.create_tweet(
    text= text
)
print(f"https://twitter.com/user/status/{response.data['id']}")
