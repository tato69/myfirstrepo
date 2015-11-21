#!/usr/bin/python
import time

print "hello, i'm first exercise, today is "  + (time.strftime("%d/%m/%Y")) + " and my master is Yoda"
people = input('how many people are there?\n')


names = []
ages = []

count = 0
while people > count:
	name = raw_input('enter your name :\n')
	names.append(name)
	age = input('enter your age :\n')
	ages.append(age)
	count = count + 1

print "\n"
print "\n"
print "\n"

print '#################################################################'
print "we are in total " + str(people) + " people\n"
count = 0
while people > count:
	print "i\'m " + names[count] + " and i\'m " + str(ages[count]) + " years old\n" 
	count = count + 1
#print "".join([str(x) for x in names] )


print "The sum of our ages is " + str(sum(ages))
print "our names are " + ', '.join(names) + "\n"
print '#################################################################'
