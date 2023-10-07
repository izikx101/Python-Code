import statistics
#list
list = [3,1,7,1,4,10]
print("List:", list)
#median
n_num = [3,1,7,1,4,10]
n = len(n_num)
n_num.sort()

if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2-1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median:" + str(median))

#mode
mode = max(set(list), key=list.count)
print("Mode:",mode)

#mean
def Average(lst):
    return sum(lst) / len(lst)
lst = [3,1,7,1,4,10]
average = Average(lst)
print("Mean:",round(average, 2))
