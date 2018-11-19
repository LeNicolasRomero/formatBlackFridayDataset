import csv
from itertools import groupby
from functools import reduce


user_ids = set()
groups = []


def keyfunc(x): return x[0]

with open("BlackFriday.csv", 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    next(reader, None)
    data = sorted(list(reader), key=keyfunc)
    for k, g in groupby(data, keyfunc):
        groups.append(list(g))

BlackFriday = []

def createUserHistory(group):
    commonInfo = group[0]
    group = sorted(group, key=lambda x: int(x[11]))
    Total = reduce(lambda purshases, purshased: int(purshases)+int(purshased[11]), group, 0)
    N_Purshased_Products = reduce(lambda acumulador, numero: acumulador+1, group, 0)
    userHistory = [
        commonInfo[0],commonInfo[2],commonInfo[3],commonInfo[4],commonInfo[7],N_Purshased_Products,Total
    ]
    BlackFriday.append(userHistory)

list(map(createUserHistory, list(groups)))

with open ('newBlackFriday.csv', mode="w") as csvfile:
    writer = csv.writer(csvfile, delimiter = ",")
    fieldnames = ['User_ID','Gender','Age','Occupation','Marital_Status','N_Purshased_Products','Total']
    writer.writerow(fieldnames)
    for row in BlackFriday:
        writer.writerow(row)
        
print(BlackFriday[0])