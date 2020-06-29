""" Divisibility Problem
 Your task is to find the minimum number of
 moves you need to do in order to make a divisible by b.
 This is possible by subtracting the remain of division of a and b from b.
 As an example can be 23 and 12
 you obtain remain 11 after dividing 23 to 12
 and after that you 12-11 such that you obtain how much steps(+1)
 you need to do to have a number divisible exactly to another
 t is the number of pairs you want to modify such that they will be divisible"""
t = int(input())


def divisibility():
    for i in range(t):
        a, b = map(int, input().split())
        if a % b == 0:
            print(0)
        else:
            print(b - a % b)


divisibility()
