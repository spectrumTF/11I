a=[int(x) for x in open("17-345.txt")]
cnt=0
mix=-200000
s=[x for x in a if x%100==52]
M=max(s)-min(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1<M)^(n2<M):
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)