#!/usr/bin/env/python
from operator import itemgetter
import sys
import operator

word=None
word_dict={}
count=None

for line in sys.stdin:
	line =line.strip()
	word,count = line.split(' ',1)
	try:
		count=int(count)
	except ValueError :
		continue

	
	if word in word_dict:
		word_dict[word]+=1
	else:
		word_dict[word] = 1


#for key,value in sorted(word_dict.items(),key = operator.itemgetter(1)):
#	print(key,value)
		

#for word in word_dict:
for key,value in sorted(word_dict.items(),key = operator.itemgetter(1)):
	print '%s\t%s' % (key,value)