a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	su=0
	for x in str(i):
		su+=int(x)
	if su%5==0:
		b=""
		e=i
		while e>0:
			b=str(e%3)+b
			e//=3
		if str(b)[2:]!="00":
			y.append(i)
print(len(y),max(y))