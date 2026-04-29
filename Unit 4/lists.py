#lists are a container data type for
#storing multiple types of data

#lists are useful for keeping data,
#organized, structured, and super-friendly

#list syntax
#to create lists, we start with a name,
#followed by the assignment operator, and
#then square brackets. Inside the brackets
#is where we put our data.

blCoding = ["intro coding", "coding 2", "ap comp sci"]
print(blCoding)

#every item in a list is called an index
#lists are organized sequentially by index position
#lists always start at zero

print(blCoding[2])

#list methods are functions that work on lists
#remember: functions just mean code instructions.

#the append method allows us to add an item at the END of a list
blCoding.append("cyber security")
print(blCoding)

#the insert method allows us to add an item ANYWHERE in a list so long as we tell in which index to pass
#it in
blCoding.insert(2,10)
print(blCoding)