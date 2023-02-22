a = [int(x) for x in open("17-257.txt")]
arrX=[]
arrY=[]
for z in a:
	if z%7==0:
		arrX.append(z)
	if z%13==0:
		arrY.append(z)
if min(arrX)>min(arrY):
	print(len(arrX),max(arrX))
else:
	print(len(arrY),max(arrY))