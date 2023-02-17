a=[int(x) for x in open("17-191.txt")]
y=[]
for i in a:
	if i%16==9 and i//16%16!=A9:
		y.append(i)
print(len(y),max(y))