a=[int(x) for x in open("17-297.txt")]
cnt=0
mix=-20000
mex=0
for i in a:
	if i%51==0:
		mex=max(mex,i)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if ((n1%10*51==n1) ^ (n2%10*51==n2)) and (n1+n2)<mex:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)