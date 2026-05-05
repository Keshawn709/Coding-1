# a FOR loop is a type of looping construct that repeats code
# instructions a specific (finite) amount of times.

# FOR loop syntax
for x in range(10):
    print('x =' + str(x))
#range() function is a special function that lets us count
#sequentially upto a certain number, even at certain intervals.

#FOR loops work really nicely with collections such as lists, because
#we may want to do something to each piece of data in a list
coworkers = ['Bill', 'Mary', 'Phillip']

for worker in coworkers:
    print(worker + 'has gotten a gift card.')

for worker in coworkers:
    if worker == 'Mary':
        coworkers.remove('Mary')
        print(coworkers)
        
prices = [10.00, 20.00, 40.00]

for item in prices:
    discount = 5.00
    item -= discount
    print(item)