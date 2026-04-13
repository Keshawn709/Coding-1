# Conditionals statements - a construct that allows
# the program to make decisions based off of the input data we give it.

# We us the IF and ELSE keywords to control
# our decisions and outcomes.

hasUmbrella = input("It's going to rain, do you have an umbrella?")

if hasUmbrella == "yes":
    print("excellent. you will be dry in the rain!")
else:
    print("You are going to get your clothes wet in the rain.")

sneakerCount = int(input("how many shoes do you have in stock?"))

if sneakerCount < 10:
    print("inventory is low, please order more shoes")
else:
    print("sell as many sneakers as you can!")


def userLogin():
    pw = int(input("what is the password?"))
    storedPw = 123
    if pw == storedPw:
        print("Congrats! You have access!")
    else:
        print("Sorry. Access revoked.")

userLogin()

#in many cases we want our programs to provide multiple outcomes
#based on the data recieved.

# The ELIF keyword, allows use to make many more conditions that can
#give us more outcomes.

def movieSelection():
    print("Here are all the movie genres we have:")
    print('1: Horror,' '2: Sci-Fi,' '3: Romance,' '4: Action')
    select = input('Please enter a number for a genre.')
    if select == 1:
        print("Scream")
    elif select == 2:
        print("Back To The Future")
    elif select == 3:
        print("The Notebook")
    elif select == 4:
        print("The Amazing Spider-Man")