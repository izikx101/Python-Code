import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
print("")
while True:
    count += 1
    userNumber = (smaller + larger) // 2
    print("%d %d" % (smaller, larger))
    print("Your number is %d" % userNumber)
    answer = input("Enter =, <, or >: ")
    if answer == "=":
        print("Hooray, I've got it in %d tries!" % count)
        break
    elif smaller == larger:
        print("I'm out of guesses, and you cheated")
        break
    elif answer == "<":
        larger = userNumber - 1
    else:
            smaller = userNumber + 1
