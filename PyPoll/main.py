import csv
import os

filePath = os.path.join('Resources', 'election_data.csv')

voteTotal = 0
candidateCount = {}
candidatePercentage = {}
printSummary = []

with open(filePath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    
    next(csvReader)
    for row in csvReader:
        candidate = row[2]
        if candidate not in candidateCount:
            candidateCount[candidate] = 1
        else:
            candidateCount[candidate] += 1
        
voteTotal = sum(candidateCount.values())
maxVotes = max(candidateCount.values())
winner = [key for key, value in candidateCount.items() if value == maxVotes]

for candidate, count in candidateCount.items():
    percentage = count/voteTotal * 100
    candidatePercentage[candidate] = percentage

candidateSummary = zip(candidateCount.items(), candidatePercentage.items())

for (candidate, count), (candidate, percentage) in candidateSummary:
    line = f"{candidate}: {percentage:.3f}% ({count})"
    printSummary.append(line)

print("Election Results\n-------------------------")
print(f"Total Votes: {voteTotal}\n-------------------------")
for candidate in printSummary:
    print(candidate)
print(f"-------------------------\nWinner: {winner[0]}\n-------------------------")

with open('analysis//results.txt', 'w') as csvResults:
    csvWriter = csv.writer(csvResults, delimiter = ',')
    csvResults.write("Election Results\n-------------------------\n")
    csvResults.write(f"Total Votes: {voteTotal}\n-------------------------\n")
    for candidate in printSummary:
        csvResults.write(candidate + "\n")
    csvResults.write(f"-------------------------\nWinner: {winner[0]}\n-------------------------")


