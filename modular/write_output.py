import os
import sys

def write_file(output,sex):
	with open(sex+'_output.txt', 'a') as the_file:
                the_file.write(output+ "\n")
	print output + " also appended to " + the_file.name
