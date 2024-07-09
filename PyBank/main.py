
import os
import csv

# Define variables & set initial values
TOTAL_MONTHS = 0
NET_TOTAL = 0
profitsLosses = [] #profits/losses
monthList = []
monthlyChanges = []

# Open & read csv file
csvpath = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")
with open(csvpath, encoding="UTF-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")  # Store the csv file header

    for row in csv_reader:
        TOTAL_MONTHS += 1
        NET_TOTAL += int(row[1])
        profitsLosses.append(int(row[1]))
        monthList.append(row[0])


# Create a list of monthly changes
firstPL = profitsLosses[0]
for i in range(1, len(profitsLosses)):
    monthlyChanges.append(profitsLosses[i] - firstPL)
    firstPL = profitsLosses[i]

AvgChange = sum(monthlyChanges) / len(monthlyChanges)

# Find max increase and min increase
MaxIncrease = max(monthlyChanges)
MaxDecrease = min(monthlyChanges)

# Find month index for the Max Increase and Max Decrease
maxIndex = minIndex = -1  # Initialize indices

for i, change in enumerate(monthlyChanges):
    if change == MaxIncrease:
        maxIndex = i + 1
    elif change == MaxDecrease:
        minIndex = i + 1
    if maxIndex != -1 and minIndex != -1:
        break  # Exit loop early if both indices are found

MaxMonth = monthList[maxIndex]
MinMonth = monthList[minIndex]

# Print results to terminal
print()
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {TOTAL_MONTHS}")
print(f"Total: ${NET_TOTAL}")
print(f"Average Change: ${round(AvgChange, 2)}")
print(f"Greatest Increase in Profits: {MaxMonth} (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")

# print results to txt file
output_path = "/Users/heather/Documents/CodeRepos/python_challenge/PyBank/Analysis/pybank_analysis.txt"
with open(output_path, "w") as f:
    print("Financial Analysis", file=f)
    print("--------------------------------", file=f)
    print(f"Total Months: {TOTAL_MONTHS}", file=f)
    print(f"Total: ${NET_TOTAL}", file=f)
    print(f"Average Change: ${round(AvgChange, 2)}", file=f)
    print(f"Greatest Increase in Profits: {MaxMonth} (${MaxIncrease})", file=f)
    print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})", file=f)