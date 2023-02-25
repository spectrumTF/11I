a=[int(x) for x in open("17-341.txt")]
cnt=0
mix=-200000
M=sum(a)/len(a)
for i in range(1,len(a)-4):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	n4=a[i+3]
	if n2*n3>n1*n4:
		mix=max(mix,n2+n3)
		if n2>M or n3>M:
			cnt+=1	
print(mix,cnt)