a=[int(x) for x in open("17-328.txt")]
cnt=0
mix=-20000
s=[int(x) for x in open("17-328.txt") if int(x)%50==0]
avg=max(s)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if str(n1+n2)==str(n1+n2)[::-1] and str(n3+n2)==str(n3+n2)[::-1] and str(n1+n3)==str(n1+n3)[::-1] and max(n1+n2,n2+n3,n3+n1)<avg:
		cnt+=1
		mix=max(mix,n1+n2+n3)
print(cnt,mix)