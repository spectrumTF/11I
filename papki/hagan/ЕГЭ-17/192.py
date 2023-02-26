s=[int(x) for x in open("17-7.txt")]
a=[]
for x in s:
    i=x
    k=0
    while i:
        k+=i%10
        i=i//10
    if k%3==0:
        a.append(x)
print(len(a),max(a))