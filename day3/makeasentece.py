import random

s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]

def sing_sen_maker():
    '''Makes a random senctence from the different parts of speech. Uses a SINGULAR subject'''
a = raw_input("Would you like to add a new word?\n")
if a.lower() == "yes":
	new_word = raw_input("Please enter a singular noun.\n")
#	s_nouns.append(new_word)
	while new_word == '':
		new_word = raw_input("The string cannot be empty! Please enter a singular noun.\n")
	print new_word, random.choice(s_verbs), random.choice(s_nouns).lower() , random.choice(infinitives)
elif a.lower() != "no":
	print "only asnwer accepted is 'yes' or 'no'"
	sing_sen_maker()
else:
	print random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() , random.choice(infinitives)

sing_sen_maker()
