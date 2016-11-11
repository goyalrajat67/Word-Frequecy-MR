#!usr/bin/env/python

import sys
import re


for line in sys.stdin:
	line=line.strip()
	if line == '':
		continue
	else:
		x=line.split(" ")
		for word in x:
			if word == '' or word == 'and' or word =='a' or word == 'an' or word == 'the' :
				continue
			else:	
				m = word
				word = word.strip(".")
				word = word.strip(",")
				print '%s %s' % (word,1)
