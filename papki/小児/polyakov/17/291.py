def conv(x,y):
	summ=""
	if x==0: return 0
	while x>0:
		summ=str(x%y)+summ
		x//=y
	return 1 if summ.count("0")==0 else 0
a=[int(x) for x in open("17-290.txt")]
cnt=0
mix=-20000
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if (abs(n1)%5==4 or abs(n2)%5==4 or abs(n3)%5==4) and (conv(n1,6) and conv(n2,6) and conv(n3,6)):
		cnt+=1
		mix=max(mix,max(n1,n2,n3)-min(n1,n2,n3))
print(cnt,mix)