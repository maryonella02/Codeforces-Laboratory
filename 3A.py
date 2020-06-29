start = input()
finish = input()
letters = 'abcdefgh'
f_ind = letters.find(finish[0]) + 1
s_ind = letters.find(start[0]) + 1

horizontal = (f_ind - s_ind)
vertical = (int(finish[1]) - int(start[1]))
print(max(abs(horizontal), abs(vertical)))
while horizontal or vertical:
    if horizontal > 0 and vertical > 0:
        horizontal -= 1
        vertical -= 1
        print("RU")
    if horizontal > 0 and vertical < 0:
        horizontal -= 1
        vertical += 1
        print("RD")
    if horizontal < 0 and vertical > 0:
        horizontal += 1
        vertical -= 1
        print("LU")
    if horizontal < 0 and vertical < 0:
        horizontal += 1
        vertical += 1
        print("LD")
    elif horizontal > 0:
        horizontal -= 1
        print("R")

    elif horizontal < 0:
        horizontal += 1
        print("L")

    elif vertical > 0:
        vertical -= 1
        print("U")
    elif vertical < 0:
        vertical += 1
        print("D")
