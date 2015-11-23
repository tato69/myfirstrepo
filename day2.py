#!/usr/bin/python

import sys
import os

def extract_num(input_str):
	if input_str is None or input_str == '':
		return 0

	out_number = ''
	for ele in input_str:
        	if ele.isdigit():
			out_number += ele
        return float(out_number)    

def usage():
	print "usage is " + sys.argv[0] + " <argument>"
	print "where argument is 'male' or 'female'\n"
	exit

def main():
	if sex == 'male' or sex == 'female':
	        print "your gender is " + sex
	
	age = raw_input('How old are you?\n')
	high = raw_input('How tall are you?\n')
	weight = raw_input('How much do you weigh?\n')

	numage = extract_num(age)
	numhigh = extract_num(high)
	numweight = extract_num(weight) 

	convage = (numage * 52)
	convhigh = ( numhigh / 30.48 )
	convweight = ( numweight * 2.2 )
	
	return "weeks " + str(convage) + " feet " + str(("%.2f" %convhigh)) + " pounds " + str(convweight)
	

if len(sys.argv) > 2:
	usage()
elif len(sys.argv) == 1:
        usage()
elif sys.argv[1] == 'male':
	sex = 'male'
	output = main()
	with open('male_output.txt', 'a') as the_file:
		the_file.write(output+ "\n")
	print output + " also appended to " + the_file.name
elif sys.argv[1] == 'female':
	sex = 'female'
	output = main()
	with open('fimale_output.txt', 'a') as the_file:
		the_file.write(output+ "\n")
	print output + " also appended to " + the_file.name
else:
	usage()

