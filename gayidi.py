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
    d = json.load(f)
    print(d)
response = client.create_tweet(
    text="دلار: " + str(d["usd"]["sell"])
)
print(f"https://twitter.com/user/status/{response.data['id']}")
