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
temp = {
    "65-75": 0,
    "75-85": 0,
    "85-95": 0,
    "95-105": 0,
    "105-115": 0,
    "115-125": 0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0
}
for range,occurence in data.items():
    if(range<=75 and range>=65):
        temp["65-75"]= temp["65-75"]+ occurence
    elif(range<=85 and range>=75):
        temp["75-85"]= temp["75-85"]+ occurence
    elif(range<=95 and range>=85):
        temp["85-95"]= temp["85-95"]+ occurence
    elif(range<=105 and range>=95):
        temp["95-105"]= temp["95-105"]+ occurence
    elif(range<=115 and range>=105):
        temp["105-115"]= temp["105-115"]+ occurence
    elif(range<=125 and range>=115):
        temp["115-125"]= temp["115-125"]+ occurence
    elif(range<=135 and range>=125):
        temp["125-135"]= temp["125-135"]+ occurence
    elif(range<=145 and range>=135):
        temp["135-145"]= temp["135-145"]+ occurence
    elif(range<=155 and range>=145):
        temp["145-155"]= temp["145-155"]+ occurence
    elif(range<=165 and range>=155):
        temp["155-165"]= temp["155-165"]+ occurence
    elif(range<=175 and range>=165):
        temp["165-175"]= temp["165-175"]+ occurence
# print(temp)
range, occurence= 0,0
for r,o in temp.items():
    if(o>occurence):
        occurence=o
        range=[int(r.split("-")[0]), int(r.split("-")[1])]
# print(range,occurence)
mode= (range[0]+range[1])/2
print('Mode: ', mode)
 
