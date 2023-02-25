a=[int(x) for x in open("17-1.txt")]
cnt=0
mix=20000
s=[int(x) for x in open("17-1.txt") if int(x)%15==0 and int(x)>0]
M=min(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if n1%2!=0 and n2%2!=0 and (n1+n2)/2>=M:
		cnt+=1
		mix=min(mix,(n1+n2)/2)
print(cnt,mix)