mix=1000
for N in range(1,1000):
	n=bin(N)[2:]
	su=0
	for i in n:
		su+=int(i)
	su=bin(su)[2:]
	if N%2==0:
		n=n+str(su)
	else:
		n="1"+n+"00"
	R=int(n,2)
	if R>215 and N<mix:
		mix=N
print(mix)