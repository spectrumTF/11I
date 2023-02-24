a=[int(x) for x in open("17-304.txt")]
cnt=0
mix=20000
s=[int(x) for x in open("17-304.txt") if int(x)%321==0]
mex=min(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if len(hex(n1)[2:])%2!=0 and len(hex(n2)[2:])%2!=0 and (n1+n2)>mex:
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)