a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	if i%10==7 or i%10==5:
		if i%9!=0 and i%11!=0:
			y.append(i)
print(len(y),max(y)+min(y))