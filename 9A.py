from fractions import Fraction


""" Die Roll
Here we have to give the probability  that Dot will won, if other two 
will roll the dice first, knowing that if Dot will give the same number she will win. 
So the probability of Dot to win is max n number from them two + n + i till 6 on 6."""
y, w = map(int, input().split())

counter = 6 - max(y, w) + 1 # find the winning possibilities of Dot.
if Fraction(counter, 6) == 1:
    print("1/1")
else:
    print(Fraction(counter, 6)) # here we find the fractional part of probability
