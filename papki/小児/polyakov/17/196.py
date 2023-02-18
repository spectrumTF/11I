a=[int(x) for x in open("17-10.txt")]
cnt=0
mix=0
for i in range(len(a)-2):
	n1=a[i]**2
	n2=a[i+1]**2
	n3=a[i+2]**2
	if (n1+n2==n3) or (n2+n3==n1) or (n1+n3==n2):
		cnt+=1
		mix+=max(a[i],a[i+1],a[i+2])
print(cnt,mix)