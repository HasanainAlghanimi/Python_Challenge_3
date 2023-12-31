import os 
import csv

budget_data = os.path.join ("/Users/hasanainalghanimi/Desktop/election_data.csv")

with open ('election_data.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next (csv_reader)

    total_votes = 0
    candidates = {}
    winner = ["", 0]

    for row in csv_reader:
        total_votes += 1
        candidate_name = 'row[3]'

        if candidate_name in candidates:
            
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

        if candidates[candidate_name] > winner[1]:
            winner = [candidate_name, candidates[candidate_name]]


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------") 




