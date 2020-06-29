"""Grow The Three
We have sticks of different lengths. We need to construct a three in xy axis, such that from (0,0)
three will end as far as possible from (0,0). It is not allowed for two consecutive sticks to be aligned simultaneously
horizontally or simultaneously vertically. The output  should be the square of the largest possible distance.

This is possible when the list of lengths are sorted in ascending order. After that list is halved.
then we form sums (that represent distance on x and y )for one axis and another according to halvings.
 This way we obtain distance y bigger than x, with whom we form square of the largest possible distance from (0,0)
 """
n = int(input())
sumx = 0
sumy = 0
stick_len = list(map(int, input().split()))
stick_len.sort()

for j in range(n):
    if j < (n // 2):
        sumx += stick_len[j]
    else:
        sumy += stick_len[j]
print((sumx * sumx) + (sumy * sumy))
