#!/usr/bin/python

x = "There are %d types of people" % 10
binary = "binary" 
do_not = "don't"
y = "Those who know %s and those who %s" %(binary, do_not)

print x
print y

print "I said: %r" % x
print "I also said: %s" % y

hilarious = True
joke_evaluation = "Isn't that joke so funny!!! %r"

print joke_evaluation % hilarious

w = "This the left side of the brain ..."
e = "This is the right side of the brain."

print w + e 
