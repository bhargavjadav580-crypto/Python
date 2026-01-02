dict = {
	"name" : "bhargav",
	"age"  : 28,
	"height" : "5feet"
}

print(dict)


##
dict1 = {
	'name' : 'bhargav',
	'age' : 20,
	'mark' : 90
}


dict2 = {
	'name' : 'bhargav1',
	'age' : 182,
	'mark' : 901
}

ans = list(dict1.keys()) + list(dict2.values())
print(ans)