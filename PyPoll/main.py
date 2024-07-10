"""Module providing a function printing python version."""
import os
import csv


#Define variables & set intial values
VOTES = 0
vote_count = []
candidates = []

#Open & read csv file, store header
csvpath = os.path.join(os.path.dirname(__file__),"Resources", "election_data.csv")
with open(csvpath, encoding="UTF-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}") #Store the csv file header


    for row in csv_reader:
        #Tally total votes
        VOTES = VOTES + 1
        #Find candidate names
        candidate = row[2]
        #Find votes per candidate
        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_count.append(1)       


#Find percentage of votes per candidate
percentages = []
most_votes = vote_count[0]
MOST_VOTES_INDEX = 0

for count in range(len(candidates)):
    vote_percentage = vote_count[count]/VOTES*100
    percentages.append(vote_percentage)
    if vote_count[count] > most_votes:
        MOST_VOTES_INDEX = count
percentages = [round (i,3) for i in percentages]


#Find the winner
winner = candidates[MOST_VOTES_INDEX]


#Print results to terminal    
print()
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {VOTES}")
print("--------------------------------")
for count, candidate in enumerate(candidates):
    print(f"{candidate}: {percentages[count]}% ({vote_count[count]})")
print("--------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------")


 #open and print results to txt file
f = open("PyPoll/Analysis/pypoll_analysis.txt", "w")
print("Election Results", file=f)
print("--------------------------------", file=f)
print(f"Total Votes: {VOTES}", file=f)
print("--------------------------------", file=f)
for count, candidate in enumerate(candidates):
    print(f"{candidate}: {percentages[count]}% ({vote_count[count]})", file=f)
print("--------------------------------", file=f)
print(f"Winner:  {winner}", file=f)
print("--------------------------------", file=f)
print()
