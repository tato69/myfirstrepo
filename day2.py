#!/usr/bin/python

import sys
import os

def usage():
	print "usage is " + sys.argv[0] + " <argument>"
	print "where argument is 'male' or 'female'\n"
	exit

def main():
	if sex == 'male' or sex == 'female':
	        print "your gender is " + sex
	
	age = input('How old are you?\n')
	high = input('How tall are you?\n')
	weight = input('How much do you weigh?\n')

	convage = (age * 52)
	convhigh = ( high / 30.48 )
	convweight = ( weight * 2.2 )
	
	return "weeks " + str(convage) + " feet " + str(("%.2f" %convhigh)) + " pounds " + str(convweight)
	

if len(sys.argv) > 2:
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

