# FOR loop- code instructions that will run infinitely under specific
#conditions, unless the condition changes.

securityCheck = 0

while securityCheck < 1:
    print("loop is running...")
    securityCheck = int(input("How many people are4 at the door?"))
    if securityCheck >= 1:
        print("sound the alarm!")