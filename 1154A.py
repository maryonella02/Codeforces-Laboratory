"""Restoring Three Numbers
You have to guess three numbers from their possible sums:
such that a+b,b+c, c+a,a+b+c as an input.
this is possible by subtracting from the biggest number the smaller three
As an example 3,6,5,4
you sort in ascending order: 3,4,5,6
and in for you subtract from the 6 - 3 = 3, from 6 - 4 = 2,
 from 6 - 5 = 1, the results are the guessed numbers. Why this occur?
 Because you subtract from a+b+c, one of the pair sums(a+b), such that
 you receive the number is not involved in the pair sum(c)"""

s = list(map(int, input().split()))
s.sort()
for i in range(3):
    print(s[3] - s[i])
