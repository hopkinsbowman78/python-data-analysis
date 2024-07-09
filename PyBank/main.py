import os
import csv

#Define variables & set intial values
MonthCount = 0
Total = 0
PL = []
monthList = []
monthlyChanges = []

# Open & read csv file
csvpath = os.path.join(os.path.dirname(__file__),"Resources", "budget_data.csv")
with open(csvpath, encoding="UTF-8") as csvfile:
   csv_reader = csv.reader(csvfile, delimiter = ',')
   csv_header = next(csv_reader)
   print(f"CSV Header: {csv_header}") #Store the csv file header
   
   for row in csv_reader:
        MonthCount += 1
        Total += int(row[1])
        PL.append(row[1])
        monthList.append(row[0])

#First month P&L value
firstPL = int(PL[0])

#This loop creates a list of monthly changes
for i in range(1, len(PL)):
    monthlyChanges.append(int(PL[i]) - firstPL)
    firstPL = int(PL[i])
    i += 1

AvgChange = sum(monthlyChanges) / len(monthlyChanges)

#Find max increase and min increase
MaxIncrease = max(monthlyChanges)
MaxDecrease = min(monthlyChanges)

#Find month index for the Max Increase and Max Decrease
for i in range(len(monthlyChanges)):
    if monthlyChanges[i] == MaxIncrease:
        maxIndex = (i + 1)
    elif monthlyChanges[i] == MaxDecrease:
        minIndex = (i + 1)
    else:
        i += 1
        
MaxMonth = monthList[maxIndex]
MinMonth = monthList[minIndex]

#Print results           
print()
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {MonthCount}")
print(f"Total: ${Total}")
print(f"Average Change: ${round(AvgChange,2)}")
print(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
 

 #open a file for writing:
f = open("/Users/heather/Documents/CodeRepos/python_challenge/PyBank/Analysis/pybank_analysis.txt","w")
print("Financial Analysis",file=f)
print("--------------------------------", file=f)
print(f"Total Months: {MonthCount}",file=f)
print(f"Total: ${Total}", file=f)
print(f"Average Change: ${round(AvgChange,2)}",file=f)
print(f"Greatest Increase in Profits: {MaxMonth}  (${MaxIncrease})",file=f)
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})",file=f)
