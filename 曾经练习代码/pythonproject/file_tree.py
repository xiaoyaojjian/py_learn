# _*_coding:utf-8_*_
# file_tree.py module containing functions to assist
# Based on the os.walk() function
import os
import re
import os.path as path

def find_files(pattern,base='.'):
	'''Finds files under base based on pattern

	Walks the file system starting at base and
	returns a list of filenames matching pattern'''
	regex = re.compile(pattern)
	matches = []
	for root,dirs,files in os.walk(base):
		for f in fiels:
			if regex.match(f):
				matches.append(path.join(root,f))
	return matches