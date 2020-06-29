"""There Are Two Types Of Burgers
You have to make two types of burgers : To assemble a hamburger
 you need two buns and a beef patty. To assemble
 a chicken burger you need two buns and a chicken cutlet.
 You have b buns, p beef patties and f chicken cutlets in your
  restaurant. You can sell one hamburger for h dollars and one
  chicken burger for c dollars. Calculate the maximum profit you
   can achieve. You have to answer t independent queries.
   The output will be the maximum profit you can achieve."""
t = int(input())
for i in range(t):
    b, p, f = map(int, input().split())
    h, c = map(int, input().split())
    if h > c:  # patties(umplutura la hamburgheri) e mai scump ca umplutura la chicken
        if b // 2 >= p:  # daca noi avem indeajuns bulocike pentru a face hamburgeri
            profit = p * h  # la profit se va adauga bani de pe hamburgeri
            b = (b // 2) - p  # aici scadem din bulocike cele pe care le-am folosit
            if b >= f: # daca da, atunci facem si chicken burgers
                profit = profit + f * c # adaugam la profit banii de pe chicken burgers
            else: # daca nu avem indeajuns bulocike
                profit = profit + b * c #facem chicken burgers din cate bulce avem si adaugam bani la profit
        else: # daca nu avem indeajuns bulocike pentru a face hamburgeri
            profit = (b // 2) * h # facem din cate bulocike aveam si putem banii la profit
    else:  # chicken (umplutura la chicken burger) e mai scump
        if b // 2 >= f: # daca avem indeajuns bulocike pentru a face chicken burger
            profit = f * c # facem si adaugam la profit
            b = (b // 2) - f # scadem din buns sa vedem cate facem mai departe
            if b >= p: # daca ave indeajuns si pentru burgeri
                profit = profit + p * h # facem si adaugam la profit
            else: # daca nu avem indeajuns buns pentru  umplutura la hamburgeri
                profit = profit + b * h # facem hamburgeri din cate buns avem
        else:# daca nu avem indeajuns buns pentru a face chicken burgers comparativ cu cata umplutura care avem
            profit = (b // 2) * c # facem doar din cate buns avem si adaugam la venit
    print(profit)
