from sys import argv

script, filename = argv

print "This is a dumb script that the hard way dude made me write"
print "It's going to be terrible"

txt = open(filename)

print txt.read()
