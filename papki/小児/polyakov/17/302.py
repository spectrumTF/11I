a=[int(x) for x in open("17-302.txt")]
cnt=0
mix=200000
mex=20000
for i in a:
	if i%21==0:
		mex=min(mex,i)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (abs((n1+n2)/2-mex)**0.5)%1==0:
		cnt+=1
		mix=min(mix,n1*n2)
print(cnt,mix)