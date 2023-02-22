a = [int(x) for x in open("17-257.txt")]
b = [int(x) for x in open("17-257.txt") if int(x)%2!=0]
sumA=max(b)
cnt=0
sum1=100000
for i in range(len(a)-1):
	if (a[i]+a[i+1])*2>sumA:
		cnt+=1
		sum1=min(sum1,a[i]+a[i+1])
print(cnt,sum1)