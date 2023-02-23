def nm(x,y):
	summ=0
	for i in str(x):
		if int(i)%2==y:
			summ+=int(i)
	return summ
a=[int(x) for x in open("17-304.txt")]
cnt=0
mix=20000
s=[int(x) for x in open("17-304.txt") if int(x)%2!=0]
mex=min(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if nm(n1,0)<nm(n1,1) and nm(n2,0)<nm(n2,1) and (n1+n2)%mex==0:
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)