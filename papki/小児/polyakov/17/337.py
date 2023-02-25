a=[int(x) for x in open("17-336.txt")]
cnt=0
mix=200000
s=[int(x) for x in open("17-336.txt") if int(x)%37==0]
M=max(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1%M==0 or n2%M==0) and (n1+n2)%M>30:
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)