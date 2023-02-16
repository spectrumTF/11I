a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	if (i%10==7 or i%10==2) and i%3==0 and i%11==0:
		y.append(i)
print(len(y),min(y))