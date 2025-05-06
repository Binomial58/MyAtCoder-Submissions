R,C=map(int, input().split())
if R==8:
    if C%2==1:
        print("brack")
    else:
        print("white")
elif R%2==1:
    if R==1 or R==15:
        print("black")
    elif R==3 or R==13:
        if C==2 and C==14:
            print("white")
        else:
            print("black")
    elif R==5 or R==11:
        if C==2 or C==4 or C==12 or C==14 :
            print("white")
        else:
            print("black")
    else:
        if C==2 or C==4 or C==6 or C==10 or C==12 or C==14 :
            print("white")
        else:
            print("black")
else:
    if R==2 or R==14:
        if C==1 or C==15:
           print("black")
        else:
            print("white")
    elif R==4 or R==12:
        if C==1 or C==3 or C==13 or C==15:
           print("black")
        else:
            print("white")
    else:
        if C==1 or C==3 or C==5 or C==11 or C==13 or C==15:
           print("black")
        else:
            print("white")