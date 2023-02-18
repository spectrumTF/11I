a=[int(x) for x in open("17-4.txt")]
cnt=0
mix=10000
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	avg=sum(a)/len(a)
	if (n1<avg and n2<avg) and abs(n1+n2)%100==19:
			cnt+=1
			mix=min(mix,n1+n2)
print(cnt,mix)