a=[int(x) for x in open("17-1.txt")]
cnt=0
mix=0
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	avg=sum(a)/len(a)
	if (n1<avg or n2<avg) and (abs(n1)%100==13 or abs(n2)%100==13):
			cnt+=1
			mix=max(mix,n1+n2)
print(cnt,mix)