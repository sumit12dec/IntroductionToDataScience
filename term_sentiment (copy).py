import sys
import json

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    results = []
    new_score = {}
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    for each in tweet_file:
        score = 0
        a = json.loads(each)
        if 'text' in a:
            a = a['text'].encode('ascii','ignore')
            b = a.split()
            for eachb in b:
	        if eachb not in scores:
			scores[eachb] = 0
			new_score[eachb]=0
	    for eachb in b:		
		score = score+ scores[eachb]
	    	if eachb in new_score:                
			new_score[eachb] = score
	    	

                #scores[eachb] = score
    for eac in new_score:
	scores[eac] = new_score[eac]
    for each in tweet_file:
        score = 0
        a = json.loads(each)
        if 'text' in a:
            a = a['text'].encode('ascii','ignore')
            b = a.split()
            for eachb in b:
                if eachb in new_score:
                    for eachbb in b:
		        score = score+ scores[eachbb]
                    new_score[eachb] = (score + scores[eachb])/tweet_file.read().count(eachb)
                    scores[eachb] = (score + score[eachb])/tweet_file.read().count(eachb)
    for each in new_score:    
        print each,new_score[each] # Print every (term, score) pair in the dictionary

if __name__ == '__main__':
    main()
