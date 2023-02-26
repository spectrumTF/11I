a=[int(x) for x in open("17-344.txt")]
cnt=0
mix=-200000
s=[x for x in a if x%103==0]
M=min(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1+n2)%2==0 and (n1-n2)%M==0:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)