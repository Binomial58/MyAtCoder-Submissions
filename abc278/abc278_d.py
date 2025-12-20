n = int(input())
A = list(map(int, input().split()))
q = int(input())
R = []
base = 0
Add = dict()
for i in range(n):
    Add[i] = A[i]
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        base = x
        Add = dict()
    elif query[0] == 2:
        i = query[1] - 1
        x = query[2]
        if i not in Add:
            Add[i] = x
        else:
            Add[i] += x
    else:
        i = query[1] - 1
        if i in Add:
            R.append(base + Add[i])
        else:
            R.append(base)
for r in R:
    print(r)
