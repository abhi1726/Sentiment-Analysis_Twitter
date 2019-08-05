{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import tweepy\n",
    "from tweepy import OAuthHandler\n",
    "from textblob import TextBlob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class TwittterClient (object):\n",
    "    \n",
    "    def __init__(self):\n",
    "        \n",
    "        \n",
    "        consumer_key=''\n",
    "        consumer_secret=''\n",
    "        access_token=''\n",
    "        access_token_secret=''\n",
    "        \n",
    "        \n",
    "        try:\n",
    "            self.auth = OAuthHandler(consumer_key, consumer_secret)\n",
    "            \n",
    "            self.auth.set_access_token(access_token, access_token_secret)\n",
    "            \n",
    "            self.api = tweepy.API(self.auth)\n",
    "        except:\n",
    "            print(\"Error: Authentication Failed\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def clean_tweet(self, tweet):\n",
    "    \n",
    "    return ' '.join(re.sub(\"(@[A-Za-z0-9]+)|([^0-9A-Za-z \\t])|(\\w+:\\/\\/\\S+)\", \" \", tweet).split())\n",
    "\n",
    "\n",
    " def get_tweet_sentiment(self, tweet): \n",
    "        \n",
    "        \n",
    "        analysis = TextBlob(self.clean_tweet(tweet)) \n",
    "        \n",
    "        if analysis.sentiment.polarity > 0: \n",
    "            return 'positive'\n",
    "        elif analysis.sentiment.polarity == 0: \n",
    "            return 'neutral'\n",
    "        else: \n",
    "            return 'negative' "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_tweets(self, query, count = 10):\n",
    "    tweets = []\n",
    "    \n",
    "    try:\n",
    "        fetched_tweets = self.api.search(q = query, count = count)\n",
    "        \n",
    "        for tweet in fetched_tweets:\n",
    "            parsed_tweet = {}\n",
    "            \n",
    "            parsed_tweet['text'] = tweet.text\n",
    "            \n",
    "            parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)\n",
    "            \n",
    "            \n",
    "            if tweet.retweet_count > 0:\n",
    "                if parsed_tweet not in tweets:\n",
    "                    tweets.append(parsed_tweet)\n",
    "            \n",
    "            else:\n",
    "                tweets.append(parsed_tweet)\n",
    "                \n",
    "            \n",
    "        return tweets\n",
    "    \n",
    "    except tweepy.TweepError as e:\n",
    "        \n",
    "        print(\"Error : \" + str(e))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    \n",
    "    api = TwitterClient()\n",
    "    \n",
    "    tweets = api.get_tweets(query = 'ABP News', count = 200)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
