"""Increasing Sequence
Output the minimal number of moves needed to make the sequence increasing.
d is the number can be increased the value by time"""
n, d = map(int, input().split())
sequence = list(map(int, input().split()))
sequence.reverse()
counter = 0
is_not_done = True

while is_not_done:
    for i in range(n-1):
        if sequence[i] <= sequence[i+1]:
            sequence[i] += d
            is_not_done = True
            counter += 1
            break
        else:
            is_not_done = False
print(counter)

