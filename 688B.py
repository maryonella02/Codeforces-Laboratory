"""
Lovely Palindromes
Here we need to form palindromes from the normal n from input.
Output should look like "n"+"reversed n". We can obtain this from
creating an reversed loop that starts from the length of the string.
Such that 10 will have lengths equal to 2 and the starting index in
this case will be 1, because range start from 0 not including the highest point.
And we will concatenate the last char with index 1 and then with index 0 and this
will form an palindrome.


"""


def palindromes():
    n = input()
    for i in reversed(range(len(n))):
        n += n[i]
    print(n)


palindromes()
