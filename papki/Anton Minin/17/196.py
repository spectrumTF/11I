n=[int(x) for x in open("17-9.txt")]
c=0
m=0
for i in range(len(n)-2):
	n1=bin(a[i])[2:]
	n2=bin(a[i+1])[2:]
	n3=bin(a[i+2])[2:]
	if int(n1.count("1")>=3 and n1.count("0")>=1) + int(n2.count("1")>=3 and n2.count("0")>=1) + int(n3.count("1")>=3 and n3.count("0")>=1)>=2:
		c+=1
		m=max(m,n[i],n[i+1],n[i+2])
print(c,m)
