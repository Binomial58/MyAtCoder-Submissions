s = input()
for i in range(ord("a"), ord("z") + 1):
    if s.count(chr(i)) == 0:
        print(chr(i))
        exit()
