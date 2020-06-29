from textwrap import wrap

"""Super Agent
Problem is about central symmetry"""
a = input() # here we take 9 chars in 3 lines as a matrix
b = input()
c = input()
abc = a + b + c# here we make a common string

s = wrap(abc, 5) # divide it in two parts in a list, first have 5, second 4 chars

s[0] = s[0][:-1] # here we delete the last char of first part, because that char is center of symmetry and has no value importance

if s[0] == s[1][::-1]: # here we compare if first is equal to second reversed
    print("YES")
else:
    print("NO")