a=[int(x) for x in open("17-335.txt")]
cnt=0
mix=-20000
s=[int(x) for x in open("17-335.txt") if int(x)%43==0]
M=min(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if ((n1+n2)%M==0) ^ (n1%10==M%10 or n2%10==M%10):
		cnt+=1
		mix=max(mix,n1,n2)
print(cnt,mix)