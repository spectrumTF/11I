a=[int(x) for x in open("17-7.txt")]
y=[]
for i in a:
	if i%8==7 and i//8%8!=2:
		y.append(i)
print(len(y),max(y))