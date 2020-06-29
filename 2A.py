"""n = int(input())
players = []
for i in range(n):
    name, score = map(str, input().split())
    players.append([name, int(score)])

sums = []

for p[0], p[1] in players:
    player_name = p[0]
    player_score = p[1]
    sums[player_name] += player_score

print(sums)"""


""" while player_
    if winner is not None:
        if player_name == winner[0]:
            winner[1] += player_score
        elif player_score > winner[1]:
            winner = p
    else:
        winner = p

print(winner[0])"""

from collections import defaultdict
n = int(input())
players = []
for i in range(n):
    name, score = map(str, input().split())
    players.append([name, int(score)])

sums = defaultdict(int)
for i, k in players:
    sums[i] += k

print(sums.items())
# output: [('a', 9), ('c', 5), ('b', 3)]

# Or if you want the key/value order reversed and sorted by key
for key, value in sorted(sums.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))

# output: [(9, 'a'), (3, 'b'), (5, 'c')]