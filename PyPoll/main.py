"""Module providing a function printing python version."""
import os
import csv

#Define variables & set intial values
votes = 0
vote_count = []
candidates = []

# Open & read csv file
csvpath = os.path.join(os.path.dirname(__file__),"Resources", "election_data.csv")
with open(csvpath, encoding="UTF-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    for row in csv_reader:
        #Tally total votes
        votes = votes + 1
        #Find Candidate Names
        candidate = row[2]
        #Tally votes per candidate
        if candidate in candidates:
           candidate_index = candidates.index(candidate)
           vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
           candidates.append(candidate)
           vote_count.append(1)


#Find percentages of votes & find the winner
percentages = []
most_votes = vote_count[0]
most_votes_index = 0
for count in range(len(candidates)):
    vote_percentage = vote_count[count]/votes*100
    percentages.append(vote_percentage)
    if vote_count[count] > most_votes:
        # print(most_votes)
        most_votes_index = count
winner = candidates[most_votes_index]
percentages = [round (i,2) for i in percentages]


#Print Election Results to terminal        
print()
print("Election Results")
print("--------------------------------")
print(f"Total Votes: {votes}")
print("--------------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})")
print("--------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------")
 

#Print Election Results to csv file
f = open("pypoll_analysis.txt", "w")
print("Election Results", file=f)
print("--------------------------------", file=f)
print(f"Total Votes: {votes}", file=f)
print("--------------------------------", file=f)
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_count[count]})", file=f)
print("--------------------------------", file=f)
print(f"Winner:  {winner}", file=f)
print("--------------------------------", file=f)