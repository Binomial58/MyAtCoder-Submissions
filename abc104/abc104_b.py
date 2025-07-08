S=input()
if S[0]=="A" and S[2:len(S)-1].count("C")==1:
    c=0
    for i in range(len(S)):
        if S[i].isupper():
            c+=1
    if c==2:
        print("AC")
    else:
        print("WA")
else:
    print("WA")