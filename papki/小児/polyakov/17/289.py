a=[int(x) for x in open("17-288.txt")]
cnt=0
mix=20000
for i in range(len(a)-3):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	n4=a[i+3]
	if (abs(n1)%10==3 or abs(n2)%10==3 or abs(n3)%10==3 or abs(n4)%10==3) and (abs(n1)%7!=3 and abs(n2)%7!=3 and abs(n3)%7!=3 and abs(n4)%7!=3):
		cnt+=1
		mix=min(mix,max(n1,n2,n3,n4)-min(n1,n2,n3,n4))
print(cnt,mix)