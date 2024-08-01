#Create a function named apply_function that takes an iterable and a function, and applies the function to each element of the iterable, returning a list of the results.

def apply_function(iterable, func):
	res = []
	for i in iterable:
		if func(i):
			res.append(i)
	return res

def func(n):
	return n > 10

ls = [12, 8, 15, 2, 6, 16]
result = apply_function(ls, func)
print(result)
