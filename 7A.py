"""Kalevitch and Chess
Here we had to find min number of rows or columns Kalevitch has to draw in black
on a chess board. """
set1 = []
counter = 0

for i in range(8):
    s = input()
    set1.append(s)  # take the input as a list of strings
for i in range(8):
    if set1[i] == 'BBBBBBBB':  # find in initial list the black row
        counter += 1  # counter to sum the number of rows to draw
if counter == 8:  # here if counter initially is equal to 8, this means that all the board should be black
    print(counter)  # and the following loop is useless
else:  # if not
    set2 = [[row[i] for row in set1] for i in range(len(set1))]  # transpose all list in list of lists of chars
    for i in range(8):
        s = "".join(set2[i])  # then join the chars to form strings as before, but transposed
        set1[i] = s
    for i in range(8):
        if set1[i] == 'BBBBBBBB':  # goes in the same loop to find the numbers of rows to draw
            counter += 1
    print(counter)
