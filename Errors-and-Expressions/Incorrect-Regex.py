import re
n=int(input())
for _ in range(n):
    exp = input()
    try:
        re.compile(exp)
        print("True")
    except:
        print("False")
