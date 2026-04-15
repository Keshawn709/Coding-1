def coinMachine():
    billAmount = int(input("Please insert total amount of money to convert!: 1, 5, 10, 20"))
    if billAmount==1:
        print("dispencing 4 quarters")
    elif billAmount==5:
        print("dispencing 20 quarters")
    elif billAmount==10:
        print("dispencing 40 quarters")
    elif billAmount==20:
        print("dispencing 80 quarters")
    else:
        print("We're sorry to inform you, but this bill amount will not be accepted.")
    

def collegeAcceptance(gpa):
    if gpa >= 3.5:
        print("We're happy to inform you that you have been accepted to Keshawn University!")
    elif gpa >= 2.8:
        print("We're happy to inform you that you have been given a conditional offer to Keshawn University!")
    else:
        print("We regret to inform you that you have not been accepted to Keshawn University.")

collegeAcceptance(3.6)