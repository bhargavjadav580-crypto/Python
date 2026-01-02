dict = {
	"name" : "bhargav",
	"age"  : 18,
	"height" : "5feet"
}

print(dict)


##
dict1 = {
	'name' : 'bhargav',
	'age' : 18,
	'mark' : 90
}


dict2 = {
	'name' : 'bhargav1',
	'age' : 181,
	'mark' : 901
}

ans = list(dict1.keys()) + list(dict2.values())
print(ans)