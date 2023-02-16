s=[int(x)for x in open('17.txt')]
b=[int(x) for x in s if x%11==0]
d=[int(x) for x in s if x%17==0]
#c=max(b)
if len(b)>len(d): a=b
else:a=d
#for i in range(len(s)-1):
 #   if s[i]>c or s[i+1]>c:
   #     a.append(s[i]+s[i+1])
print(len(a),min(a))