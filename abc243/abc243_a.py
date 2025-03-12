V,A,B,C=map(int, input().split())
while V>=0:
    V-=A
    if V<0:
        print("F")
    else:
        V-=B
        if V<0:
            print("M")
        else:
            V-=C
            if V<0:
                print("T")