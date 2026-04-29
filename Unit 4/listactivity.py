customerSatisfaction = [1,2,3,4,5]

def classCsat(grade):
    if grade == customerSatisfaction[0]:
        print("1/5 this was a poor class.")
    elif grade == customerSatisfaction[1]:
        print("2/5. Could be better.")
    elif grade == customerSatisfaction[2]:
        print("3/5. Not good. Not bad.")
    elif grade == customerSatisfaction[3]:
        print("4/5. Pretty good!")
    elif grade == customerSatisfaction[4]:
        print("5/5! Excellent!!")
    else:
        print('cant find value')


#1. The append list method only let's us put an item at the END of the list.
#Insert list method let's us put ANYWHERE on the list.
grocerylist = ['milk', 'pizza', 'carrots', 'water','chicken breast']
grocerylist.append('fruit punch')
print(grocerylist)

grocerylist = ['milk', 'pizza', 'carrots', 'water','chicken breast']
grocerylist.insert(3, 'pancakes')

numbers= [200, 2302, 1, 10, 42, 0, 400, 5, 20]
numbers.sort()
print(numbers)