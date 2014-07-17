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
    temp = {}
    for each in tweet_file:
        score = 0
        a = json.loads(each)
        if 'text' in a:
            a = a['text'].encode('ascii','ignore')
            b = a.split()
	    for eachb in b:
		
		if eachb not in scores:
			score = score+0
		else:
			score = score+scores[eachb]
	    for eachbi in b:
		#if eachbi=="friend": print a,score
		total_occ=0
		if eachbi not in scores:			
			total_occ = total_occ + 1
			if eachbi in temp:
				ai = temp[eachbi]
				if score>0:
					ai[0] = ai[0] + score
				if score<0:
					ai[1] = ai[1] + score
				ai[2] = ai[2] + total_occ
				temp[eachbi] = ai
			else:
				ai=[0,0,0]
				ai[0] = ai[0]+score
				ai[1] = ai[1] + score
				ai[2] = ai[2]+total_occ
				temp[eachbi] = ai

    for ev in temp:
	ab = temp[ev]
	#if float(ab[1])/ab[2]!=0:
	scorer = (float(ab[0])+ab[1])/ab[2]
	#else:
	#	scorer=0
	#if ev=="friend":
	print ev, scorer
	
if __name__ == '__main__':
    main()
