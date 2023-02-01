def fun(s):
  n=list(map(int,str(s)))
  s1=sum(i for i in n if i%2==0)
  s2=sum(n[::2])
  return abs(s1-s2)
c=1
while True:
  if fun(c)==28:
    print(c)
    break
  c+=1

