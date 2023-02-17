a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	b=int(str(i)[-2:-1])+int(str(i)[-1:])
	if b>=15:
		if i%3!=0 and i%4!=0 and i%7!=0:
			y.append(i)
print(min(y),sum(y))