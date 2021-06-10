import sys
import csv
import tweepy


#Get your Twitter API credentials and enter them here
consumer_key = 'Your consumer key'
consumer_secret = 'Your consumer secret key'
access_key = 'Your access key'
access_secret = 'Your access secret key'

#method to get a user's last tweets
def get_tweets(username):

	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to the number of tweets you want
	number_of_tweets = 100
	
	#get tweets
	tweets_for_csv = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = username).items(number_of_tweets):
		tweets_for_csv.append([username, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")])

	#write to a new csv file from the array of tweets
	outfile = username + "_tweets.csv"
	print("writing to " + outfile)
	with open(outfile, 'w+') as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerows(tweets_for_csv)

def main():
	if len(sys.argv) == 2:
		get_tweets(sys.argv[1])
	else:
		print("Error: enter one username")
        

if __name__ == '__main__':
	main()
	


