n, m = map(int, input().split())
set1 = []

min_i = n
max_i = -1
min_j = m
max_j = -1
for i in range(n):
    s = input()
    set1.append(s)
for i in range(n):
    for j in range(m):
        if set1[i][j] == '*':
            if i < min_i:
                min_i = i
            if i > max_i:
                max_i = i
            if j < min_j:
                min_j = j
            if j > max_j:
                max_j = j
for min_i in range(max_i + 1):
    for min_j in range(max_j + 1):
        print(set1[i][j])


# set2 = [[row[i] for row in set1] for i in range(m)]
# print(set2)# transpose all list in list of lists of chars
# for i in range(len(set2)):
#     s = "".join(set2[i])  # then join the chars to form strings as before, but transposed
#     set2[i] = s
#
# set2 = [j for j in set2 if '*' in j]
#
# print(set2)
# set1 = [[row[i] for row in set2] for i in range(len(set2))]
# for i in range(len(set1)):
#     s = "".join(set1[i])  # then join the chars to form strings as before, but transposed
#     set1[i] = s
#
# set1 = [j for j in set1 if '*' in j]
# print(*set1, sep="\n")