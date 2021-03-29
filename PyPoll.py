data = []
with open('election_data.csv') as file:
    for line in file.readlines():
        li = line.split(',')
        try:
            data.append([int(li[0]), li[1], li[2].rstrip()])
        except ValueError:
            pass


print('Election results')
print('-'*25)

votes = len(data)
print(f'Total votes: {votes}')
print('-'*25)

candidate_votes = {}

for i in data:
    if i[2] not in candidate_votes:
        candidate_votes[i[2]] = 1
    else:
        candidate_votes[i[2]] += 1

for candidate in candidate_votes:
    print(f'{candidate}: {(candidate_votes[candidate]/votes):.3%} ({candidate_votes[candidate]})')

print('-'*25)
max_votes = max(candidate_votes.values())
for candidate in candidate_votes:
    if candidate_votes[candidate] == max_votes:
        winner = candidate
print(f'Winner: {winner}')
print('-'*25)
