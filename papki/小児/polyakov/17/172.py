a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	if bin(i)[-4:]=="1001":
		b=""
		e=i
		while e>0:
			b=str(e%5)+b
			e//=5
		if b[-2:]=="11":
			y.append(i)
print(max(y),sum(y))