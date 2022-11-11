import csv
import sys
head = []
allRowList = []
with open(sys.argv[1], 'r') as file:
    reader = csv.reader(file, delimiter = ';')
    ncol = len(next(reader))
    for rIndex,row in enumerate(reader):
        #head.insert(1,row[rIndex])
        rowList = []
        for cIndex,ncol in enumerate(row):
            #print(row[cIndex])
            rowList.append(row[cIndex])
        allRowList.append(rowList)
        #print("-")
#print(allRowList)


with open('OUTPUT.csv', 'w') as file:
    writer = csv.writer(file, delimiter = ',')
    finalRows = []
    writer.writerows(list(zip(allRowList[0],allRowList[1],allRowList[2])))
        



