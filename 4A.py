"""Watermelon
From Mister Bostan course we know that odd number can't be the sum of two even numbers
So I put the condition if number is odd and smaller than 3, because 2 is even, but when divided is 1+1"""

w = int(input())
if w < 3 or w % 2 != 0:
    print("NO")
else:
    print("YES")
