def check(x,y):
	if (x+y)**0.5%1==0:
		return 1
	return 0
a=[int(x) for x in open("17-316.txt")]
cnt=0
mix=-20000
avg=sum(a)/len(a)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if (check(n1,n2) or check(n1,n3) or check(n3,n2)) and (n1+n2+n3)/3>avg:
		cnt+=1
		mix=max(mix,n1+n2+n3)
print(cnt,mix)