# savings = 0
# goal = 1000
# while savings < goal:
#     print("you currently have:" + str(savings))
#     deposit = int(input("how much do you want to add?"))
#     savings += deposit
#     print("you have  " + str(savings) + "in your account")
#     if savings >= goal:
#         print("Congrats! You have enough for your trip!")
#     else:
#         print("Keep saving.")


# My Own Work
myPassword = "keshawn132"

def myPassword ():
    myPassword = input("what is your password?")
    while myPassword != "keshawn132":
        if myPassword == "keshawn132":
            print("Congrats! You have access!")
        else:
            print("Please try again.")
