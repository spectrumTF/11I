def check(x):
	x=oct(x)[2:]
	if "7" in x:
		return 0
	return 1
a=[int(x) for x in open("17-328.txt")]
cnt=0
mix=-20000
s=[int(x) for x in open("17-328.txt") if int(x)%2!=0]
avg=sum(s)/len(s)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if check(n1+n2) and check(n2+n3) and check(n1+n3) and (n1+n2+n3)<avg:
		cnt+=1
		mix=max(mix,n1+n2+n3)
print(cnt,mix)