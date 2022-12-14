from flask import Flask, render_template, request
import tweepy

# I added this based on the additional question to hide api credentials
import os

app = Flask(__name__)

# Enter your Twitter API credentials here.
# Modified for api credential hiding in an env file.
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an API object
api = tweepy.API(auth)

@app.route('/')
def index():
    # Get the user's screen name from the form
    screen_name = request.args.get('screen_name')

    # Get the user's tweets
    tweets = api.user_timeline(screen_name=screen_name, count=10)

    return render_template('index.html', tweets=tweets)

if __name__ == '__main__':
    app.run()