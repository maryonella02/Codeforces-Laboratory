"""Sasha and Sticks
The easiest one
Shortly is about n sticks that will be crossed in the number of k
at one time. you loose if you have not enough k sticks at the
end to cross. Sasha is first and he wants to know if he will win.
To find out this you need to find the result of dividing n with k. If the result is even, he loose
because he will remain with n % k sticks at the end. If result is odd, this means that he win, because he start first
 and Lena remain with n % k sticks to cross, not enough for continuing the play."""
n, k = map(int, input().split())


def sasha():
    rest = n // k
    if (n // k) % 2 == 0:
        print("NO")
    else:
        print("YES")


sasha()
"""As an example is 10 sticks with 4 stick per time to cross.
Sasha start, and 6 sticks are left. Lena cross 4 sticks and Sasha loose because he remains with 2 sticks. 
The output will be NO."""
