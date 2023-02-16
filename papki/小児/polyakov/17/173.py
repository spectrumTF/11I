a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	if i%3==0 and i%9!=0:
		if i%10>=4: y.append(i)
print(len(y),int(sum(y)/len(y)))