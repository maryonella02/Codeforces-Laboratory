"""Candies Division
Shortly I am Santa and I want
to distribute candies in such way that max half of the number of children
will have with one more candy than others.
 As an example I have 19 candies to distribute to 4 children
 Initially, I find that each children will have 4 candies equally
 after that I find how many candies I have to give in this case 4 candies to each
 4 cildren = 16 candies. Then I find how many candies remain = 3.
 Then I half the number of children to find how many kids can have with one more in plus
 I get 2 children. After that I compare how many kids can have one more candy with
  how many candies remain and choose the smaller number, because if I have more candies
  than available kids I need to respect the condition with half of the kids.
  If I have more kids, but not enough remaining candies, I can divide one candy for 2 or more kids.
  Sooo, from this comparing I find how many more candies I can to distribute. """

t = int(input())


def santa():
    for i in range(t):
        a, b = map(int, input().split())
        max_candies = a // b  # we find how many candies each kid will have
        max_candies *= b  # how many candies will take kids equally
        extra_candies = a - max_candies #here we find extra candies
        # now we have to respect the condition that not more than half of the kids
        # will have more with one than another half, so we divide the number of kids
        half = b // 2

        max_candies += min(half, extra_candies) # here we "give to one half the kids, one more candy"
        print(max_candies)


santa()

