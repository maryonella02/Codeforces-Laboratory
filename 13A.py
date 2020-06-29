from fractions import Fraction

a = int(input())
base = 0
total_sum = 0

def convert(a, base):
    if a == 0:
        return '0'
    nums = []
    while a:
        a, r = divmod(a, base)
        nums.append(str(r))
    return ''.join(reversed(nums))


for i in range(1, a - 1):
    base = a - i
    for c in convert(a, base):
        total_sum += int(c)
b = str(Fraction(total_sum, a - 2))
if b.find('/') != -1:
    print(b)
else:
    print(f"{b}/1")

