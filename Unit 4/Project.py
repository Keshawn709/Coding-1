# Arizona Prices
# My app allows the user to give a certain amount of money to get
#an Arizona.

def arizonaPrices():
    print("Watermelon = 1.00")
    print("Sweet Tea = 1.50")
    print("Green Tea = 2.00")

    userSelect = input("Please select an item!")
    if userSelect == "Sweet Tea":
        print("You've just selected Sweet Tea! Please insert 1.50 to get your drink!")
        userInsert = input