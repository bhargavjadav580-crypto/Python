#Convert tuple of tuples into a single flat tuple.


t = ((1, 2), (3, 4), (5, 6))

flat = ()

for i in t:
	flat = flat + i
	
print(flat)
 