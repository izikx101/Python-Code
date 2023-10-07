lyst = [3, 1, 7, 1, 4, 10]
def mean(mylyst):
    average = 0
    for item in mylyst:
        average = average + item
    average = average/len(mylyst)
    return average

def mode(mylyst):
    uniquenumbers = []
    for item in mylyst:
        if item not in uniquenumbers:
            uniquenumbers.append(item)
        repeatednumber = 0
        numberofrepeats = 0
        for item in uniquenumbers:
            repeats = 0
            for item2 in mylyst:
                if item == item2:
                    repeats = repeats + 1
            if repeats > numberofrepeats:
                repeatednumber = item
                numberofrepeats = repeats
        return repeatednumber

def median(mylyst):
    mylyst.sort()
    length=len(mylyst)
    if length%2 ==1:
        return mylyst[(length-1)//2]
    else:
        return (mylyst[length//2-1] + mylyst[length//2])/2
    
print("List:",lyst)
print("Mode:",mode)
print("Median:",median)
print("Mean:",mean)
