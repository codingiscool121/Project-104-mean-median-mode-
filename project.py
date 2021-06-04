import pandas as pd
import csv
from collections import Counter

with open('HeightWeight.csv') as f:
    read = csv.reader(f)
    list1 = list(read)
random = list1.pop(0)
list2 = []
for i in range(len(list1)):
    temp = list1[i][1]
    list2.append(float(temp))
total=0

for i in list2:
    total=total+i
mean=total/len(list1)
print("Mean:", mean)

list3 = []

for i in range(len(list1)):
    temp=list1[i][2]
    list3.append(float(temp))

list3.sort()
length2=len(list2)

if(length2%2 == 0):
    median1 = float(list2[length2//2])
    median2 = float(list2[length2//2 - 1])
    finalmedian = (median2)
    print("Median: ", finalmedian)
else:
    finalmedian = list2[length2//2]
    print("Median: ", finalmedian)


list4 = []
for i in range(len(list1)):
    temp = list1[i][1]
    list4.append(float(temp))
data = Counter(list4)
print("Mode but not really:", data)