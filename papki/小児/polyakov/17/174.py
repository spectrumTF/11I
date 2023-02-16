a=[int(x) for x in open("17-4.txt") if int(x)>100]
y=[]
for i in a:
	if i%100//10<=4:
		if 3<=i%1000//100<=7: y.append(i)
print(len(y),min(y))