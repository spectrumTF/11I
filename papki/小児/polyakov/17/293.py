a=[int(x) for x in open("17-292.txt")]
cnt=0
mix=20000
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if abs(n1%17-n2%17)==n1%4+n2%4:
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)