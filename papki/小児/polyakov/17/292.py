a=[int(x) for x in open("17-292.txt")]
cnt=0
mix=-20000
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if n1%6+n2%6==n1%11+n2%11:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)