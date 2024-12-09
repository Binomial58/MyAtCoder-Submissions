S_AB,S_AC,S_BC=input().split()
if S_AB==">":
    #A>B
    if S_AC==">":
        #A>C
        if S_BC==">":
            #B>C
            print("B")
        else:
            #C>B
            print("C")
    else:
        #C>A
        print("A")
else:
    #B>A
    if S_BC==">":
        #B>C
        if S_AC==">":
            #A>C
            print("A")
        else:
            #C>A
            print("C")
    else:
        #C>B
        print("B")