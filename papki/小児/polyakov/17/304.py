def nm(x):
	summ=0
	for i in str(x):
		summ+=int(i)
	return summ
a=[int(x) for x in open("17-304.txt")]
cnt=0
mix=0
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if ((n1%nm(oct(n2)[2:])==0)^((n2%nm(oct(n1)[2:]))==0)) and (n1+n2)%min(a)==0:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)