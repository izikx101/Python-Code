import math
initialnumber = int(input("Enter the initial number of organisms: "))
rateGrowth = float(input("Enter the rate of growth [ a real number > 1]: "))
numberHours = int(input("Enter the number of hours it takes to achieve this rate of growth: "))
totalHours = int(input("Enter the total hours of growth: "))
initialnumber = initialnumber * rateGrowth
rateGrowth = rateGrowth / numberHours
numberHours = numberHours * totalHours
tp = initialnumber * rateGrowth / totalHours * numberHours * 2
print("The total population is:", tp)
