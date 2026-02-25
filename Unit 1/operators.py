# Operator - a way for data types to
# interact and do things.

# Assignment Operator Family
"assignment operators assign values to variables"
"values = data types"
# "we represent the assignment operator"
# "with a SINGLE equal sign"

name = "Keshawn"
score = 90
inSchool = True

# Comparison Operator Family
# comparison operators are used to compare values
# values = data = data types
# when you run code using comparisons it'll return as true or false

print(10 < 2)
print(10 == 10) # 2 EQUAL SIGNS MEAN AS
print(10 != 2) # NOT THE SAME
print(9 >= 1) # greater/less than OR EQUAL

print("Keshawn" == "Keshawn")#computers are VERY literal
#("Keshawn" == "keshawn") is WRONG (cause the 2nd Keshawn has a lowercase "k")

# Arithematic Operator Family
# Arithematic is just mathmatical operations
print(2 + 2)

print(3 * 5)

print(10 / 2)

# Logical Operator Family
# we use these constructs to evaluate conditions
# to see whether they are true or false

# AND - checks to see if two conditions are true. 
# If both are true, the result is true

print(2 > 1 and 6 > 2)

attendance = 0
gpa = 3.8

print( attendance <= 0 and gpa > 3.5)

# OR - checks to see if only 1 condition is true.
# If 1 condition is true, the result will be true.

print(attendance <= 0 or gpa > 3.5)

# NOT - evaluates the conditions and returns the opposite result

print(not(attendance <= 0 and gpa > 3.5))
