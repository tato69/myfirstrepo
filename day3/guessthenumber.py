import os
from random import randint

global number
global inum

def setrandom():
	global number
	number = (randint(1,100))
	print number

print "guess the number"
inum = input("number pls\n")
setrandom()

while number != inum :

	if inum > number :
		print "mmmmm not good... fly down" 
	elif inum < number :
		print "come on man be tough! go higher"
	inum = input("once again\n")

print "finally! you did it!"
