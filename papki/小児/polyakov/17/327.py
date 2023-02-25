def cvrt(x,y):
	res=""
	while x>0:
		res=str(x%y)+res
		x//=y
	return res

a=[int(x) for x in open("17-324.txt")]
cnt=0
mix=-20000
s=[int(x) for x in open("17-324.txt") if int(x)%37!=0]
avg=sum(s)/len(s)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if cvrt(n1+n2+n3,2)==cvrt(n1+n2+n3,2)[::-1] and min(n1,n2,n3)>avg:
		cnt+=1
		mix=max(mix,n1+n2+n3)
print(cnt,mix)