x1, y1, x2, y2 = map(int, input().split())
R = []
l = [x2 - x1, y2 - y1]
l = [-l[1], l[0]]
R.append(x2 + l[0])
R.append(y2 + l[1])
l = [-l[1], l[0]]
R.append(R[0] + l[0])
R.append(R[1] + l[1])
print(*R)
