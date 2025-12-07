x, k, d = map(int, input().split())
# マイナスの方向に行くと絶対値が減る場合
if abs(x - d) <= abs(x + d):
    l = x // d
    if k <= l:
        print(abs(x - k * d))
    else:
        # 残っている移動回数
        o = k - l
        if o % 2 == 0:
            print(abs(x - d * l))
        else:
            print(abs(x - d * (l + 1)))
else:
    l = -x // d
    if k <= l:
        print(abs(x + k * d))
    else:
        # 残っている移動回数
        o = k - l
        if o % 2 == 0:
            print(abs(x + d * l))
        else:
            print(abs(x + d * (l + 1)))
