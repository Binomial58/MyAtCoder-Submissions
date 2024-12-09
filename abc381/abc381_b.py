S = input()
A = list(S)
N = len(S)

# 奇数長の場合は即座にNoを出力
if N % 2 == 1:
    print("No")
else:
    # 隣接する要素が異なるかチェック
    for i in range(0, N, 2):
        if A[i] == A[i + 1]:
            continue
        else:
            print("No")
            exit()
    # 重複するペアがないかチェック
    for j in range(0, N, 2):
        for k in range(j + 2, N, 2):
            if A[j] == A[k]:
                print("No")
                exit()
    # すべての条件を満たした場合
    print("Yes")