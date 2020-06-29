"""Margarite and the best present
We have a list : -1, 2, -3, 4, -5, ...We have to find sum
from starting position l to ending position r, inclusive."""
q = int(input())


def margarita():
    for i in range(q):
        l, r = map(int, input().split())
        if l % 2 == 0:
            sum1 = l // 2
        else:
            sum1 = l // 2 - (l - 1)
        if r % 2 == 0:
            sum2 = r // 2
        else:
            sum2 = r // 2 - r
        print(sum2 + sum1)


margarita()
