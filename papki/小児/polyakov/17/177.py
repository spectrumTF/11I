a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	b=str(i).count("0")
	if b>=2:
		if i%7==0:
			y.append(i)
print(max(y),len(y))