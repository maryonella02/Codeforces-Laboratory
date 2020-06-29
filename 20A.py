import re
n = input()
to_remove = "/" #char to be de-dublicated
pattern = "(?P<char>[" + re.escape(to_remove) + "])(?P=char)+" # "match any character from to_remove that appears more than once in a row"
n = re.sub(pattern, r"\1", n) # replaces that match with the first group, which is only one character long.
if n[-1] == "/" and len(n) > 1: # if string is bigger than 1 and have at the end "/"
    n = n[:-1] # strip the last char
print(n)

