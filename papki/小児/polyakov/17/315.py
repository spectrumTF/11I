a=[int(x) for x in open("17-304.txt")]
cnt=0
mix=20000
mex=sum(a)/len(a)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if bin(n1*n2)[2:].count("101010")>=1 and (n1+n2)>mex:
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)