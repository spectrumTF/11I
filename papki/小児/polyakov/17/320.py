def check(x,y):
	if x%2==0 and y%2==0:
		if (x+y)%100==44:
			return 1
	return 0
a=[int(x) for x in open("17-316.txt")]
cnt=0
mix=20000
s=[int(x) for x in open("17-316.txt") if int(x)%202==0]
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if (check(n1,n2) or check(n1,n3) or check(n3,n2)) and n1+n2+n3>max(s):
		cnt+=1
		mix=min(mix,n1+n2+n3)
print(cnt,mix)