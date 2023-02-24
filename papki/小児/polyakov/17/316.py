def check(n1,n2):
	a1=[n1//10==n2//10,(str(n1//100)+str(n1%10))==(str(n2//100)+str(n2%10)),(str(n1//1000)+str(n1%100))==(str(n2//1000)+str(n2%100)),n1%1000==n2%1000]
	return 1 if any(a1) else 0
a=[int(x) for x in open("17-316.txt")]
cnt=0
mix=20000
mex=0
for x in range(len(a)-1):
	for y in range(x,len(a)):
		mex=max(mex,x+y)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if ((check(n1,n2) and n1!=n2) or (check(n1,n3) and n1!=n3) or (check(n2,n3) and n2!=n3)) and (n1+n2+n3)<mex:
		cnt+=1
		mix=min(mix,n1+n2+n3)
print(cnt,mix)