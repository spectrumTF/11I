Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=[int(x) for x in open('17-257.txt')]
a=[]
z=[x for x in s if x%10==4]
for i in range(len(s)-1):
    if s[i]+s[i+1]<max(z)+min(z):
        a.append(s[i]+s[i+1])
print(len(a),max(a))