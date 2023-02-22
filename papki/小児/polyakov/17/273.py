a=[int(x) for x in open("17-273.txt")]
avg=max(a)
cnt=0
minn=20000
maxx=-20000
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if (n1+n2+n3)<avg:
			cnt+=1
			maxx=max(maxx,n1,n2,n3)
			minn=min(minn,n1,n2,n3)
print(cnt,maxx+minn)