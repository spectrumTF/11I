s=[int(x) for x in open('17-7.txt')]
a=[]
for i in range(len(s)):
    x=s[i]
    k=0
    while x:
        k+=x%10
        x=x//10
    if k%3==0:
        a.append((s[i]))
print(len(a),max(a))