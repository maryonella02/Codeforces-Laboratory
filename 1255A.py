""" Changing Volume
We have two input data a and b. A is start, b the finish, you need to find
the minimum m=number of steps used to reach B, such that steps are of six types:
(−5,−2,−1,+1,+2,+5). In the problem I take the distance (absolute value) and start dividing it by the biggest steps.
Variable step is counter of divisions.  """

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    k = abs(a - b) #iau distanta
    step = 0
    m = k // 5 #impart distanta la cel mai mare pas 5
    k -= (5 * m) #scad din distanta cat s-a impartit
    step += m # adaug la step cat s-a impartit din distanta

    m = k // 2 #impart distanta la 2
    k -= (2 * m) # scad din distanta cat s-a putut imparti
    step += m # adaug la step de cate ori s-a impartit distanta la doi

    step += k #aici dupa toate calculele ar trebui sa fie in distanta ori 1 ori 0 si asta se adauga la step
    print(step)
    
"""De exemplu:
a = 5,  b = 12.
k = 7
m = 7 // 5 = 1
K -= 5 * 1 = 2
step += m = 1
m = k // 2 = 2 // 2 = 1
k -= (2 * m) = 2 - 2 = 0
step += m = 1 + 1
step += k = 2 + 0"""