import sys
import json

def main():
	tweet_file = open(sys.argv[1])
	hash_score = {} # initialize an empty dictionary
	sorted_hash_score = {}
	for each in tweet_file:
		a = json.loads(each)
		if 'entities' in a:
			h = a['entities']
			b = h["hashtags"]
			for each_dict in b:
				hashtag = each_dict['text'].encode('ascii','ignore')
				if hashtag not in hash_score:
					hash_score[hashtag]=1
				else:
					hash_score[hashtag] = hash_score[hashtag] +1
	sorted_hash_score = sorted(hash_score.items(), key=lambda x: x[1])
	#	sorted_hash_score[w] = hash_score[w]
	#for each_hashtag in sorted_hash_score:
	#	print each_hashtag, sorted_hash_score[each_hashtag]
	print sorted_hash_score
if __name__ == '__main__':
    main()
