def check(x):
	x=int(oct(x)[2:])
	arr=[]
	while x!=0:
		arr.append(x%10)
		x//=10
	arr=arr[::-1]
	if arr.index(min(arr))>arr.index(max(arr)):
		return 1
	return 0
a=[int(x) for x in open("17-340.txt")]
cnt=0
mix=-200000
s=[int(x) for x in a if x%22==0]
M=sum(s)/len(s)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if check(n1) and check(n2) and n1+n2<M:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)