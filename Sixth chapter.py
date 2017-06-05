import easygui
user_response = easygui.msgbox("Hello There!")
print user_response
'OK'

import easygui
flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
                           choices = ['Vanilla','Chocolate','Strawberry'])
easygui.msgbox ("You picked " + flavor)

import easygui
flavor = easygui.choicebox("What is your favorite ice cream flavor?",
                           choices = ['Vanilla','Chocolate','Strawberry'])
easygui.msgbox ("You picked " + flavor)
