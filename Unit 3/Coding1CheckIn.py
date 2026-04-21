#You've been tasked with creating a program that charges a fee based on the number of eggs they purchase.  
# Your program should take in the number of eggs being purchases as an argument. 
# When a user passes in a number (the number of eggs being bought), 
# the program should charge a fee of 1.15 per egg (for ex. 1 egg= 1.15, 2 eggs = 2.0, 3 eggs= 3.45, etc.) 

#If the 6 or more eggs are purchases the price of the egg is changed from 1.15 to 1.00 (ex. 6 = 6.00, 7 = 7.00, etc.)

#also, if the number of eggs is more than 12, the new price per egg should be .75. 

#lastly, if a person is buying more than 20 eggs, inform the user that they cannot buy that many eggs at 1 time. 

def costofEggs():
    print("How many eggs would you like to buy?")
    eggsBought = ('1 egg = 1.15')