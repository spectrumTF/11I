a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	if i%5==3 and i%9==5 and i%8!=7:
		y.append(i)
print(len(y),max(y))