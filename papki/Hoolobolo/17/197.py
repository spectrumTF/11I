a=[int(x) for x in open('17_196.txt')]
b=[]
for i in range(len(a)-1):
    if ((1000>(a[i]+a[i+1])>99)and ((a[i]+a[i+1])%10>(a[i]+a[i+1])//10%10)):
        b.append(a[i]+a[i+1])
print(len(b),min(b))
