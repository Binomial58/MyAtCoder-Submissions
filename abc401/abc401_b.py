n = int(input())
count = 0
login = False
for i in range(n):
    s = input()
    # print(s, login)
    if s == "login":
        login = True
    elif s == "logout":
        login = False
    elif s == "private" and not login:
        count += 1
print(count)
