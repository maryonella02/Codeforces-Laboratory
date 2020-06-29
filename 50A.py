"""Domino piling
You are given a rectangular board of M × N squares. Also you are given an unlimited
 number of standard domino pieces of 2 × 1 squares.
 You are asked to place as many dominoes as possible on the board so as to meet the following conditions:
1. Each domino completely covers two squares.
2. No two dominoes overlap.
3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.
From the following conditions you can understand that you need to find the area of the board
and divide it by two, because each domino occupies 2 squares"""
a, b = map(int, input().split())
print(a * b // 2)
