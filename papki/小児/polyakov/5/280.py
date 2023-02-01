for N in range(1,20000000):
	S1=0
	for i in str(N):
		i=int(i)
		if i%2!=0:
			S1+=i
	S2=0
	for i in range(len(str(N))-1,-1,-1):
		if i%2==0:
			S2+=int(str(N)[i])
	R=abs(S1-S2)
	if R==29:
		print(N)
		break