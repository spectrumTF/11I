a=[int(x) for x in open("17-10.txt")]
c=0
m=10000
for i in range(len(a)-1):
	s=a[i]+a[i+1]
	if len(str(s))==3:
		if (s%10)>(s%100//10):
			c+=1
			m=min(m,s)
print(c,m)
