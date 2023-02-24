def nm(x,y):
	summ=0
	for i in str(x):
		if int(i)%2==y:
			summ+=1
	return summ
a=[int(x) for x in open("17-304.txt")]
cnt=0
mix=-20000
mex=max(a)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if nm(n1,0)==nm(n1,1) and nm(n2,0)==nm(n2,1) and (n1+n2)>mex:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)