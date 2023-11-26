import csv

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

file_path = 'election_data.csv'

with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
