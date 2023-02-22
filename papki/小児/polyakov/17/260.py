a = [int(x) for x in open("17-257.txt")]
b = [int(x) for x in open("17-257.txt") if int(x)%10==4]
sumA=max(b)+min(b)
cnt=0
sum1=0
for i in range(len(a)-1):
	if (a[i]+a[i+1])<sumA:
		cnt+=1
		sum1=max(sum1,a[i]+a[i+1])
print(cnt,sum1)