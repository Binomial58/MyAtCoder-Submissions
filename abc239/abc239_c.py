a,b,c,d=map(int, input().split())
t=[0,0]
s=[abs(c-a),abs(d-b)]
if s==[0,4] or s==[2,4] or s==[3,1] or s==[2,0] or s==[1,3] or s==[3,3] or s==[4,2] or s==[0,2] or s==[4,0] or s==[1,1]: 
    print("Yes")
else:
    print("No")