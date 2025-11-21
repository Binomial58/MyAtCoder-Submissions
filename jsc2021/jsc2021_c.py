a,b=map(int, input().split())
m=0
for i in range(1,b+1):
	q=a%i
	if q!=0:
		q=i-q
	if a+q+i<=b:
		m=max(m,i)
print(m)