a=[int(x) for x in open("17-336.txt")]
cnt=0
mix=200000
find=0
s=[int(x) for x in open("17-336.txt") if int(x)%8==0 and int(x)!=8]
M=min(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if n1%M==0 and n2%M==0:
		cnt+=1
		if n1+n2<mix:
			mix=n1+n2
			find=max(n1,n2)
print(cnt,find)