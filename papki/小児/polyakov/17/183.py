a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	if i%16==11:
		if i%7==0 and i%6!=0 and i%13!=0 and i%19!=0:
			y.append(i)
print(sum(y),len(y))