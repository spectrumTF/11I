a=[int(x) for x in open("17-304.txt")]
cnt=0
mix=20000
avg=sum(a)/len(a)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (len(oct(n1))%2!=0 or len(oct(n2))%2!=0) and (n1+n2)>avg:
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)