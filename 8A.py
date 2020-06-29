default = input()
first = input()
second = input()
if first in default and second in default:
    if default.find(first) < default.find(second) < default.rfind(first):
        print("both")
    elif default.find(first) < default.find(second):
        print("forward")

    elif default.find(first) > default.find(second):
        print("backward")
    else:
        print("fantasy")
else:
    print("fantasy")
