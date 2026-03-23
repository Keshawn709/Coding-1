# Conditional Logic - a special class of function that
# lets us run specific instructions based on specific
# data

# we use the if and else keywords to run different
# instructions

# Conditional Syntax - how to write a conditional block
absences = 0

if absences == 0:
    print("you have a dress down day.")
    #if is the condition we're looking for

else:
    print("you must come in uniform.")
    #else is our default/exit. what we want to happen
    #if we CANT find the data we are looking for

creditsToPass = 30
currentCredits = int(input("how many credits do you have?"))
if currentCredits < creditsToPass:
    print('sorry you dont have enough credits')
else:
    print("congrats you are graduating this year")

schoolYear = input("What year of High School are you in?")

if schoolYear == 'freshman':
    print('you will be taking intro to high school and you have to do certain things')
elif schoolYear == 'sophmore':
    print('you have to take state testing')
elif schoolYear == 'junior':
    print('you need an intership')
else:
    print('sorry this info does not apply to you.')