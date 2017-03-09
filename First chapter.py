print "I love pizza!"
print "pizza" * 20
print "yum" * 40
print "I'm full."
print "Hello, and welcome to Phyton!"
print "I hope you will enjoy learning program."
print "Bye for now!"

print "Try it out"
print '''num modo interativo, use o Python para calcular os minutos na semana'''
print 1440 * 7

print "My name is Harue Matsumoto "
print "I was born on September 18, 1984 "
print "My favorite color is purple."

import random

secret = random.randint (12, 44)
guess = 0
tries = 0

print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
print "It's a number from 1 to 99. I'll give you 6 tries. "

while guess != secret and tries < 6:
    guess = input (" What's yer guess? ")
    if guess < secret:
        print "Too low, ye scurvy dog!"
    elif guess > secret:
            print "Too high, landlubber!"
            tries = tries + 1
    if guess == secret:
        print "Avast! Ye got it! Found my secret, ye did!"
    else:
        print "No more guesses! Better luck next time, matey!"
        print "The secret number was" , secret


















