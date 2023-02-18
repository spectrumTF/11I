a=[int(x) for x in open("17-202.txt")]
cnt=0
mix=10000
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if not(n1>0 and n1%10==5 and len(str(n1))==3) and (n2>0 and n2%10==5 and len(str(n2))==3) and not(n3>0 and n3%10==5 and len(str(n3))==3):
			cnt+=1
			mix=max(mix,n1+n2+n3)
print(cnt,mix)