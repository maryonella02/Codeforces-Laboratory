""" Bachgold Problem
Given a positive integer n represent it as
a sum of maximum possible number of prime numbers. What does it mean?
  n can be represented in an n//2 number of 2 if even,
 if odd the last number will be 3"""
import sys

n = int(input())
print(n // 2)
if n % 2 == 0:
    for i in range(n // 2):
        sys.stdout.write("2 ")

if n % 2 == 1:
    for i in range(n // 2 - 1):
        sys.stdout.write("2 ")
    sys.stdout.write("3 ")
