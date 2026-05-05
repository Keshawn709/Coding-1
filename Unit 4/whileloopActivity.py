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

def passwordLoop():
    myPassword = "keshawn132"
    userPassword = input("what is your password?")
    while myPassword != userPassword:
            print("Please try again.")
            if myPassword == myPassword:
                print("Congrats! You have access!")
