a=[int(x) for x in open("17-276.txt")]
cnt=0
mix=-20000
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	for x in range(2,1000):
		if (n1*x==n2 and n2*x==n3) or (n1*x==n3 and n3*x==n2) or (n2*x==n1 and n1*x==n3) or (n2*x==n3 and n3*x==n1) or (n3*x==n1 and n1*x==n2) or (n3*x==n2 and n2*x==n1):
			cnt+=1
			mix=max(mix,x**2)
print(cnt,mix)