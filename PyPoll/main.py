"""Module providing a function printing python version."""
import os
import csv
os.system('clear') #clear the terminal prior to running the program

#Open & read csv file, print the header

csvpath = os.path.join(os.path.dirname(__file__),"Resources", "election_data.csv")
with open(csvpath, encoding="UTF-8") as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter = ',')
    print(f"CSV Header: {csv_reader.fieldnames}")


  #Create a dictionary for candidate_info, initialize vote count
    candidate_info={}
    VOTES=0


#Loop rows to find data
    for row in csv_reader:
        if row['Candidate'] in candidate_info.keys(): 
            #Find candidate names
            candidate_info[row['Candidate']]+=1
        else:
            candidate_info[row['Candidate']]=1
        #Find total number of votes
        VOTES+=1

# Initialize & store results in "output" for printing
output=''
output += '\n'
output += 'Election Results\n'
output += '----------------------------\n'
output += f'Total Votes: {VOTES}\n'
output += '----------------------------\n'

#Calculate and store number & percent of votes per candidate
for name in candidate_info:
    #Find number of votes for each candidate
    candidate_votes=candidate_info[name]
    #Find percent of votes for each candidate
    percent_vote=((candidate_info[name]/VOTES)*100)
    output += f'{name}:, {percent_vote:.3f}%, ({candidate_votes})\n'

#Find and store the winner
winner=max(candidate_info, key=candidate_info.get)

output += '----------------------------\n'
output += f'Winner:{winner}\n'
output += '----------------------------\n'
output += '\n'

#Print results to terminal
print(output)

#Print results to txt file
f = open("Analysis/pypoll_analysis.txt", "w")
print(output, file=f)
