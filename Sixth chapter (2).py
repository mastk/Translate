import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?")
easygui.msgbox("You entered" + flavor)

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                          default = 'Vanilla')
easygui.msgbox ("You entered" + flavor)

import easygui
name = easygui.enterbox("What is your name?")
easygui.msgbox("You entered" + name)

import easygui
housenumber = easygui.enterbox("What your housenumber?")
easygui.msgbox("You entered" + housenumber)

import easygui
streetname = easygui.enterbox(" What is your streetname?")
easygui.msgbox("You entered" + streetname)

import easygui
neighborhood = easygui.enterbox("What is your neighborhood?")
easygui.msgbox("You entered" + neighborhood)

import easygui
postalcode = easygui.enterbox ("What is your postalcode?")
easygui.msgbox("You entered" + postalcode)


import random, easygui
secret = random.randint (12, 44)
guess = 0
tries = 0

easygui.msgbox (" " "AHOY! I'm the Dread Pirate Roberts, and I have a secret:It's a number from 1 to 99. I'll give you 6 tries." " ")

while guess != secret and tries < 6:
    guess = easygui.integerbox(" What's yer guess,matey?")
    if not guess: break
    if guess < secret:
        easygui.msgbox (str(guess) + "is too low, ye scurvy dog!")
    elif guess > secret:
            easygui.msgbox (str(guess) + "is too high, landlubber!")
    tries = tries + 1
    if guess == secret:
        easygui.msgbox("Avast! Ye got it! Found my secret, ye did!")
    else:
            easygui.msgbox("No more guesses! Better luck next time, matey!")
