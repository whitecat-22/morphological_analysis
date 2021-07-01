import tweepy
import time
import os

# TwitterAPIKey(https://developer.twitter.com/en/portal/projects-and-apps)
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

# OAuth認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

total_tweets = ''
last_id = None

# 検索キーワード
search_word = os.environ.get("SEARCH_WORD")

# 検索
search_results = api.search(q=search_word, count=100)

# 最初の100件のツイート本文を文字列結合
for search_result in search_results:
    total_tweets += search_result._json['text']
    print(search_result._json['text'])
    last_id = search_result._json['id']

# 100件目毎のツイートIDをlast_idに入れて、2週目以降は毎回それ以降のIDのみ検索(検索被り防止)
for i in range(100):
    time.sleep(1)
    search_results2 = api.search(q=search_word, count=100, max_id=last_id)
    for search_result2 in search_results2:
        total_tweets += search_result2._json['text']
        last_id = search_result2._json['id']
print(total_tweets)

# ファイル出力
with open('search_tweets.txt', mode='a') as f:
    f.write(total_tweets)
