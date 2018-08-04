#!/usr/bin/env python

import sys

for line in sys.stdin:
	matrix_index, row, col, value = line.rstrip().split(",")
	if matrix_index == "A":
		for i in range(5):
			key = row + "," + str(i)
			print "%s\t%s\t%s"%(key,col,value)
	else:
		for j in range(5):
			key = str(j) + "," + col
			print "%s\t%s\t%s"%(key,row,value)
