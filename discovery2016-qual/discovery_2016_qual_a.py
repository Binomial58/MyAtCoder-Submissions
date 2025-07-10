W=int(input())
S="DiscoPresentsDiscoveryChannelProgrammingContest2016"
c=0
while c<51:
    print(S[c:min(c+W,51)])
    c+=W
