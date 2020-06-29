""" Longest Regular Bracket Sequence
We have to Print the length of the longest substring that is a regular
bracket sequence, and the number of such substrings.
"""
s = [-1] #This task can be solved by using stacks.
stored = 0
rep = 0

for i, c in enumerate(input()):
    if c == '(': #when we get '('
        s.append(i) #we push it to stack
    else: # When we get ')'
        if len(s) > 1: # if there are present '(' in stack
            s.pop() # pop the last
            current = i - s[-1] # get the length of sequence was regular
            if current > stored: # here we set the max value of total brackets closed at the moment
                stored = current # here is stored in another variable, to be in future compared with the current
                rep = 1 # here is counter of presence
            elif current == stored: # if present value of total closed brackets is equal with previous
                rep += 1  # this means that they are repeating
        else: #if there is only one element in stack
            s[0] = i #  starting point to measure length has shifted to position i
if stored:
    print(stored, rep)

else:
    print(0, 1)

