a=[int(x) for x in open("17-328.txt")]
cnt=0
mix=20000
s=[int(x) for x in open("17-328.txt") if int(x)%50==0]
avg=sum(s)/len(s)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if (n1+n2)**0.5%1==0 and (n3+n2)**0.5%1==0 and (n1+n3)**0.5%1==0 and min(n1+n2,n2+n3,n3+n1)>avg:
		cnt+=1
		mix=min(mix,n1+n2+n3)
print(cnt,mix)