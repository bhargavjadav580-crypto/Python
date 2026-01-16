#FIND NUMBER BETN 40 TO 5 THAT DIVISIBLE BY 4 AND 8


x=range(40,4,-1)
for i in x:
	if(i%4==0 and i%8==0):
		print(i) 