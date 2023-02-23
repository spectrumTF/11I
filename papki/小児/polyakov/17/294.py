def nm(x):
	summ=0
	for i in str(x):
		summ+=int(i)
	return summ
a=[int(x) for x in open("17-294.txt")]
cnt=0
mix=-20000
avg=sum(a)/len(a)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if ((nm(n1)+nm(n2))**0.5)%1==0 and (n1+n2)>avg:
		cnt+=1
		mix=max(mix,nm(n1)+nm(n2))
print(cnt,mix)