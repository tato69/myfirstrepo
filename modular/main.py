import os
import sys

from extract_number import *
from usage import *
#from write_output import sex
from write_output import *

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
	write_file(output,sex)
elif sys.argv[1] == 'female':
	sex = 'female'
	output = main()
	write_file(output,sex)
else:
	usage()
