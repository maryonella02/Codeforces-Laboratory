"""Kana and Dragon Quest game
Dragon has X points of life.
You need to kill the dragon by two types of hits: n = x // 2 + 10
and m = x - 10.
From input you have x points of dragon's life, n changes to kill using n and m changes to kill
using m.
From my point of view is better to kill the dragon with hit n but till
the moment x > 20, because this lead to more steps in vane, for this
I introduces min() function to choose the smallest from the last two values
of x. When number of n provided are over. We find if number of m will be enough to kill
the dragon (m * 10) >= x. Why bigger or equal, because if this number will be bigger, x of
the dragon will decrease with m * 10 life points.

"""

t = int(input())


def dragon():
    for i in range(t):
        x, n, m = map(int, input().split())
        for i in range(n):
            y = x
            z = x // 2 + 10
            x = min(z, y)

        if (m * 10) >= x:
            print("YES")
        else:
            print("NO")


dragon()
