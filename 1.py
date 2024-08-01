#Create a Python function named my_map that mimics the behavior of Python’s built-in map() function. The function should take a function and an iterable, apply the function to each item in the iterable, and return a list of the results.
#Requirements:
#	Return a list of results instead of using a generator.
#	Include type annotations and a detailed docstring explaining how the function works.
#	Do not use the built-in map() in your implementation.

def my_map(func: int, iterable: list) -> list:
	'''
	my_map function takes each element in iterable and applies on them the some function which is applied to func argument.
	Our function takes two arguments:
		func which returns an integer
		iterable which returns list
	1) First our function creates a list object named 'res', to whom it will append elements with power of two
	2) Then it creates for loop in iterable which takes each element of iterable
	3) Then it appends to our 'res' list elements to whom was earlier applied some() function
	4) After that it returns updated 'res' list

	some() function returns number with power of two

	Example:
		result = my_map(some, [1, 2, 3, 4, 5])
		print(result)
	Output:
		[1, 4, 9, 16, 25]
	'''
	res = []
	for i in iterable:
		res.append(func(i))
	return res


def some(x):
	return x ** 2


result = my_map(some, [1, 2, 3, 4, 5])
print(result)
