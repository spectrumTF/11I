def nmsm(x):
	numsum=0
	for i in str(abs(x)):
		numsum+=int(i)
	return numsum
a=[int(x) for x in open("17-272.txt")]
b=[int(x) for x in open("17-272.txt") if int(x)>0]
avg=sum(b)/len(b)
cnt=0
mix=-20000
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if n1>avg or n2>avg:
			cnt+=1
			mix=max(mix,nmsm(n1),nmsm(n2))
print(cnt,mix)