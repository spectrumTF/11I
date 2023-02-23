def conv(x,y):
	converter=""
	while x>0:
		converter=str(x%y)+converter
		x//=y
	return converter
a=[int(x) for x in open("17-278.txt")]
cnt=0
mix=-20000
soom=0
for x in a:
	if abs(x)%32==0:
		soom+=conv(abs(x),5).count("3")*3
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if n1>soom or n2>soom or n3>soom:
		cnt+=1
		mix=max(mix,n1+n2+n3)
print(cnt,mix)