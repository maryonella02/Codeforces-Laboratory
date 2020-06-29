"""Flag
Rows should be different, every char in row identical.
If rules are respected  output yes, if not no."""
n, m = map(int, input().split()) # take the number of columns and rows
flag = []
counter = 1
for i in range(n):
    s = input()
    flag.append(s) #take as input every rows
for x in range(1, n):
    if flag[x] == flag[x - 1]: # verify if rows are different ot not
        counter += 1 # counter increment if rules are ignored

for x in range(n):
    for y in range(m):
        if flag[x][y] != flag[x][y-1]: # verify if every char is different or not
            counter += 1


if counter > 1: # if counter bigger that 1 , this means that rules are not respected
    print("NO")
else:
    print("YES")
