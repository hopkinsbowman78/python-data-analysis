"""Module providing a function printing python version."""
import os
import csv
os.system('clear') #clear the terminal prior to running the program


#Initialize variables and lists to store data
TOTAL_MONTHS = 0
NET_TOTAL = 0
profitsLosses = []
monthList = []
monthlyChanges = []

# Open & read csv file, print header
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")
with open(csvpath, encoding="UTF-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

#Find the total months, net total and lists of months and profits & losses
    for row in csv_reader:
        TOTAL_MONTHS += 1
        NET_TOTAL += int(row[1])
        profitsLosses.append(int(row[1]))
        monthList.append(row[0])

#Store data for printing later
output=''
output += '\n'
output += 'Financial Analysis\n'
output += '----------------------------\n'
output += f'Total Months: {TOTAL_MONTHS}\n'
output += f'Total: ${NET_TOTAL}\n'


# Create and store list of monthly changes
firstPL = profitsLosses[0]
for i in range(1, len(profitsLosses)):
    monthlyChanges.append(profitsLosses[i] - firstPL)
    firstPL = profitsLosses[i]

#Find and store average of monthly changes
avgChange = sum(monthlyChanges) / len(monthlyChanges)
#Print average change
output += f'Average Change: ${round(avgChange, 2)}\n'

# Find max increase and min increase
maxIncrease = max(monthlyChanges)
maxDecrease = min(monthlyChanges)

# Find month index for the Max Increase and Max Decrease
MAX_INDEX = MIN_INDEX = -1  # Initialize indices

for i, change in enumerate(monthlyChanges):
    if change == maxIncrease:
        MAX_INDEX = i + 1
    elif change == maxDecrease:
        MIN_INDEX = i + 1
    if MAX_INDEX != -1 and MIN_INDEX != -1:
        break  # Exit loop early if both indices are found

maxMonth = monthList[MAX_INDEX]
minMonth = monthList[MIN_INDEX]

#Store Greatest Increase in Profits
output += f'Greatest Increase in Profits: {maxMonth} (${maxIncrease})\n'
#Store Greatest Decrease in Profits
output += f'Greatest Decrease in Profits: {minMonth} (${maxDecrease})\n'

#print results to terminal
print(output)

#Print results to txt file
f = open("Analysis/pybank_analysis.txt", "w")
print(output, file=f)

