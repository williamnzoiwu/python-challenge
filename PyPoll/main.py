#Dependencies
import os
import csv
from collections import Counter

#variables
candidates = []
votes = []

#Set path for file
csvpath = os.path.join( "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #go through candidates
    for row in csvreader:
        candidates.append(row[2])

    sort = sorted(candidates)
    candidates_sorted = sort

    #count votes for each candidate
    vote_count = Counter (candidates_sorted)
    votes.append(vote_count.most_common())

    for item in votes:
        first = format((item[0][1])*100/(sum(vote_count.values())),'.3f')
        second = format((item[1][1])*100/(sum(vote_count.values())),'.3f')
        third = format((item[2][1])*100/(sum(vote_count.values())),'.3f')
           
#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {sum(vote_count.values())}")
print("-------------------------")
print(f"{votes[0][0][0]}: {first}% ({votes[0][0][1]})")
print(f"{votes[0][1][0]}: {second}% ({votes[0][1][1]})")
print(f"{votes[0][2][0]}: {third}% ({votes[0][2][1]})")
print("-------------------------")
print(f"Winner: {votes[0][0][0]}")
print("-------------------------")

#export text file
with open('pypoll.txt', "w") as f:

    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {sum(vote_count.values())}\n")
    f.write("-------------------------\n")
    f.write(f"{votes[0][0][0]}: {first}% ({votes[0][0][1]})\n")
    f.write(f"{votes[0][1][0]}: {second}% ({votes[0][1][1]})\n")
    f.write(f"{votes[0][2][0]}: {third}% ({votes[0][2][1]})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {votes[0][0][0]}\n")
    f.write("-------------------------\n")
