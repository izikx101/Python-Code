message = input("Enter a message: ")
distanceValue = int(input("Enter the distance value: "))
result = ""
for x in message:
    result += chr(ord(x)+distanceValue)
    print(""+result)
