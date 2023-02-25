a=[int(x) for x in open("17-338.txt")]
cnt=0
mix=-200000
M=min(a)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if n1%117==M or n2%117==M:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)