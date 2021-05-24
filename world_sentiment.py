import tweepy
from textblob import TextBlob
import preprocessor as p
import statistics
from typing import List

# consumer_key = "" 
# consumer_secret = ""
# cant show this, sorry ^
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

#getting tweets , specifically ten of them 
def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode ='extdended',  lang='en').items(10):
        all_tweets.append(tweet.full_text)

    return all_tweets


#cleaning tweets gotten from function above
def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean=[]
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
    return tweets_clean


#getting the sentiment of the tweets 
def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

def generate_average_sentiment_score(keyword: str) -> int:
    #getting the tweets
    tweets = get_tweets(keyword)

    #clean the tweets AGAIN
    tweets_clean = clean_tweets (tweets)
    sentiment_scores = get_sentiment(tweets_clean)

    average_score = statistics.mean(sentiment_scores)


    return average_score

if __name__ == "__main__":
    print("what does the world prefer")
    first_thing = input()
    print("..or...")
    second_thing = input()
    print("\n")

    first_score = generate_average_sentiment_score(first_thing)
    second_score = generate_average_sentiment_score(second_thing)

    if (first_score > second_score):
        print(f"Humanity prefers {first_thing} over {second_thing}")
    else:
        print(f"Humanity prefers {second_thing} over {first_thing}")


 
