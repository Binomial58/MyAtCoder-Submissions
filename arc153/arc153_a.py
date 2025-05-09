N=int(input())
S=0
for a in range(1,10):
     for j in range(100):
        if j <10:
            j="0"+str(j)
        else:
            j=str(j)
        for b in range(10):
            for c in range(10):  
                for i in range (10):   
                    S+=1
                    if S==N:
                        print(str(a)+str(a)+j+str(b)+str(b)+str(c)+str(i)+str(c))
                        exit()