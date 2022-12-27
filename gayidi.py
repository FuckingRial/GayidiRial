import tweepy,json,os,requests


consumer_key = os.environ.get("CK")
consumer_secret = os.environ.get("CS")
access_token = os.environ.get("AT")
access_token_secret = os.environ.get("ATS")

def send(bot_message):
       bot_token = os.environ.get("TOKEN")
       send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=@gayidirial&parse_mode=Markdown&disable_web_page_preview=true&text=' + bot_message
    
       response = requests.get(send_text)
    
       return response.json()

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
btcrial = int(int(btc["stats"]["btc-rls"]["dayClose"])/10)
dollarrial = int(emruz["usd"]["sell"])
btcdollar = int(btc["global"]["binance"]["btc"])
text = "دلار: " + str(f"{dollarrial:,}") + " تومن\n بیتکوین: " +str(f"{btcrial:,}") + " تومن\n بیتکوین: " + str(f"{btcdollar:,}") + " دلار"
if emruz["usd"]["sell"] > diruz["usd"]["sell"]:
    text = text + "\n\n امروز " +str(round(100*(emruz["usd"]["sell"] - diruz["usd"]["sell"])/ diruz["usd"]["sell"],2)) + " درصد فقیر تر شدیم "

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)
api.update_status_with_media(text,filename="weekplot.png")

#telegram
print(send(text.replace("\n","%0A")))
