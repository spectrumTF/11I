def conv(x,y):
	summ=""
	while x>0:
		summ=str(x%y)+summ
		x//=y
	return len(summ)
a=[int(x) for x in open("17-290.txt")]
cnt=0
mix=-20000
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if (abs(n1)%5==1 or abs(n2)%5==1 or abs(n3)%5==1) and (conv(n1,6)==4 and conv(n2,6)==4 and conv(n3,6)==4):
		cnt+=1
		mix=max(mix,max(n1,n2,n3)-min(n1,n2,n3))
print(cnt,mix)