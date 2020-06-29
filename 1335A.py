""" Candies and Two Sisters
Here you should distribute the total number of candies
such that one sister will get more than another.
Output should contain the number of all possibilities
to distribute candies.
The algorithm consists of halving exactly the total number
, and after that subtracting one from the even one
As an example can be 7, you divide it and obtain 3,
because a=6, b=1
a=5, b=2
a=4, b=3  => exactly 3 possibilities, as we obtained."""

"t is the number of the sets of candies to distribute"
t = int(input())


def sisterhood():
    for i in range(t):
        n = int(input())
        if n % 2 == 0:
            print(n // 2 - 1)
        else:
            print(n // 2)
    return


sisterhood()
