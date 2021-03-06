import sys
import json

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    results = []
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
                if eachb in scores:
                    score = score+ scores[eachb]
            results.append(score)
    for each in results:    
        print each # Print every (term, score) pair in the dictionary

if __name__ == '__main__':
    main()
