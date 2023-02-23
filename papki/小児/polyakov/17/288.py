a=[int(x) for x in open("17-288.txt")]
cnt=0
mix=20000
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if abs(n1)%7!=abs(n2)%7 and abs(n2)%7!=abs(n3)%7 and abs(n1)%7!=abs(n3)%7 and (n1<0 or n2<0 or n3<0):
		cnt+=1
		mix=min(mix,max(n1,n2,n3)-min(n1,n2,n3))
print(cnt,mix)