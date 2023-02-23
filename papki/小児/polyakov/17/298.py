a=[int(x) for x in open("17-298.txt")]
cnt=0
mix=-20000
mex=0
for i in a:
	if i%197==0:
		mex=max(mex,i)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if  ( (str(int(n1/197)) in str(n1) and (n1/197)%1==0) ^ (str(int(n2/197)) in str(n2) and (n2/197)%1==0))and (n1+n2)<mex:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)