n, m, a = map(int, input().split())

# we need to find out how many flagstones are needed to pave along n part.
length = n // a
# then we need to find out how many flagstones are needed to pave along m part.
width = m // a

"""above, we found exactly how many tiles will cover length and width, but 
 our calculations can be wrong , because if the division is not exact, this mean
that some space remain uncovered. So we add some conditions"""
if n % a != 0:  # this mean that some space is not covered
    length += 1  # and is needed one more flagstone to cover space
# the same condition need to be done for width

if m % a != 0:
    width += 1

# in the end we need to multiply this data (to find area) to find out the minimal possible number to tile

print(length * width)
