a=[int(x) for x in open("17-303.txt")]
cnt=0
mix=0
M=0
need=0
for i in a:
	for x in range(25):
		if x**3==i:
			M=max(M,i)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	tg=abs(M-(n1+n2+n3))
	if tg%2==0 and (tg**0.5)%1==0:
		cnt+=1
		if (n1+n2+n3)>mix:
			mix=n1+n2+n3
			need=n1*n2*n3/max(n1,n2,n3)
print(cnt,need)