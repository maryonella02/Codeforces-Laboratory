"""Triangle
It's all about 7 grade math. Need to find if an triangle can be formed.
Input consists of 4 lengths of sticks.
We sort in descending order, because we need to compare the bigger lengths with smaller.
And start to compare the sum of two smaller with the bigger in two iterations, because
 we don't know what stick need to be excluded to make a conclusion.
 """

triangle = list(map(int, input().split()))
triangle.sort(reverse=True)
normal = 0
degenerated = 0
monster = 0
for i in range(2):
    if triangle[i] < triangle[i+1] + triangle[i+2]:
        normal += 1
    elif triangle[i] == triangle[i+1] + triangle[i+2]:
        degenerated += 1
    else:
        monster += 1
if normal > 0:
    print("TRIANGLE")
elif degenerated > 0:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")