a=[int(x) for x in open("17-353.txt")]
cnt=0
mix=-200000
M=(max(a)+min(a))/2
for r1 in range(int(len(a)*0.5)+1):
		x=a[r1]
		y=a[len(a)-r1-1]
		if (x>M and y<M)^(x<M and y>M):
			cnt+=1
			mix=max(mix,x+y)
print(cnt,mix)