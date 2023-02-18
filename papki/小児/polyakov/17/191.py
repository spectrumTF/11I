a=[int(x) for x in open("17-7.txt")]
y=[]
for i in a:
	if i%16==9 and i//16%16!=10:
		y.append(i)
print(len(y),max(y))