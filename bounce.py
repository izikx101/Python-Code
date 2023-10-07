height = int(input("Enter the height from which the ball is dropped: "))
bounceindex = float(input("Enter the bounciness index of the ball: "))
numberOfbounces = float(input("Enter the number of times the ball is allowed to continue bouncing: "))
distance=0
while numberOfbounces > 0:
    distance = distance + height
    height = height * bounceindex
    distance = distance + height
    numberOfbounces-= 1
print("Total distance traveled is: ", distance, "units")
