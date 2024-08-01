#Create a function named my_filter that behaves like Python’s built-in filter() function. It should filter items out of an iterable based on a function that returns either True or False and return a list of the filtered items.
#Requirements:
#	Return a list of filtered items instead of using a generator.
#	Include type annotations and a detailed docstring.
#	Avoid using the built-in filter() in your implementation.

def my_filter(func: int, iterable: list) -> list:
	'''
	my_filter function takes each element in iterable and filters elements depending on the some() function
	Our function takes two arguments:
		func, which returns an integer
		iterable which returns a list
	1) First our function creates list object named 'res' to whom it will append iterable's elements
	2) Then it creates for loop in iterable, which takes each element of it
	3) It checks if each elements after passing some() function's statement is true
	4) After checking it appends filtered elements to 'res' list
	5) After all this my_filter returns 'res' list

	some() function returns number if it's module is equal to 0

	Example:
		result = my_filter(some, [1, 2, 3, 4, 5, 6])
		print(result
	Output:
		[2, 4, 6])
	'''
	res = []
	for i in iterable:
		if func(i):
			res.append(i)
	return res

def some(x):
	return x % 2 == 0

result = my_filter(some, [1, 2, 3, 4, 5, 6])
print(result)
