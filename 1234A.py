"""Equalize Prices Again
Here you have a sequance to divide to its length, such that you will not less than you have before dividing"""
q = int(input())

for i in range(q):
    n = int(input()) # take the length of sequence
    sum = 0
    x = list(map(int, input().split())) # take the sequence
    for j in range(n):
        sum += x[j] #calculate the sum of all values
    if sum % n == 0: # if sum is divided to length without remainder
        print(sum // n) # no changes are made
    else:# if not
        print(sum // n + 1) # add to dividing 1, because you need to have not smaller than you have
