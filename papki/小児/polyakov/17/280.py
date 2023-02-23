def conv(x,y):
	converter=""
	while x>0:
		converter=str(x%y)+converter
		x//=y
	return converter
a=[int(x) for x in open("17-278.txt")]
cnt=0
mix=20000
soom=0
for x in a:
	soom+=conv(abs(x),8).count("7")*7
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if n1>soom and n2>soom:
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)