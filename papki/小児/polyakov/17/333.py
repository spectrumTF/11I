def nm(x):
	summ=0
	for i in str(x):
		summ+=int(i)
	return summ

a=[int(x) for x in open("17-333.txt")]
cnt=0
mix=-20000
s=[int(x) for x in open("17-333.txt") if int(x)//10000==0 and  int(x)//1000>0]
avg=sum(s)/len(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if not((n1+n2) in a) and n1+n2<avg:
		cnt+=1
		mix=max(mix,nm(n1)+nm(n2))
print(cnt,mix)