a=[int(x) for x in open("17-281.txt")]
cnt=0
mix=-20000
for i in range(len(a)-5):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	n4=a[i+3]
	n5=a[i+4]
	n6=a[i+5]
	for x in range(1,500):
		if ((n1*x==n2 and n2*x==n3) and (n4+x==n5 and n5+x==n6)) or ((n1+x==n2 and n2+x==n3) and (n4*x==n5 and n5*x==n6)):
			cnt+=1
			mix=max(mix,n1+n2+n3+n4+n5+n6)
print(cnt,mix)