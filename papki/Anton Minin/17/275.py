Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=[int(x) for x in open('17-275.txt')]
a=[]
for i in range(len(s)-1):
    if (abs(s[i])+abs(s[i+1]))%11==0:
        a.append(s[i]+s[i+1])
print(len(a),max(a))