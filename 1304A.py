"""Two Rabbits
You have to find a moment in time (in seconds) after
which the rabbits will be at the same point, knowing the initial position
of first rabbit x, the position y  of the second rabbit and the distance they hope
respectively a and b.
So the problem is solved when you find the distance y - x between rabbits
and you divide it to the total distance (a + b) they hope in one second
If no remainder remains, this means that they will meet together in the second that correspond to the product of division
of total distance(y - x) to distance performed in one second(a + b).
If there is remainder after division this means that they don't meet at the same place."""
t = int(input())


def rabbits():
    for i in range(t):
        x, y, a, b = map(int, input().split())
        if (y - x) % (a + b) == 0:
            print((y - x) // (a + b))
        else:
            print(-1)


rabbits()
