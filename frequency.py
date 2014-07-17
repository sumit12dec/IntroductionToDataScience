import sys
import json

def main():
    tweet_file = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    total_words = []
    freq = {}
    temp = {}
    all_count = 0
    for each in tweet_file:
        a = json.loads(each)
        if 'text' in a:
            a = a['text'].encode('ascii','ignore')
            b = a.split()
	    total_words.extend(b)
	    #print len(total_words)
    total_count = len(total_words)
    for e in total_words:
	if e not in freq:
    		freq[e] = total_words.count(e)/total_count
    for eachh in freq:
	print eachh, freq[eachh]
    	
if __name__ == '__main__':
    main()
