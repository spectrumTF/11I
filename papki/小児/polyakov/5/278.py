for N in range(1,10000000):
	S1=0
	for i in str(N):
		i=int(i)
		if i%2!=0:
			S1+=i
	S2=0
	for i in range(1,len(str(N))+1):
		if i%2!=0:
			S2+=int(str(N)[i-1])
	R=abs(S1-S2)
	if R==31:
		print(N)
		break