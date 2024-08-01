#Develop a function called my_zip that combines elements from multiple iterables into tuples, similar to the built-in zip() function, and returns a list of these tuples.
#Requirements:
#	The function should stop zipping when the shortest iterable is exhausted and return a list of tuples.
#	Include type annotations and a detailed docstring.
#	Do not use the built-in zip() in your code.

def my_zip(*iterables: list) -> list[tuple]:

	'''
	my_zip function combines elements from lists by each index and outputs them in list. This function outputs tuple inside list
	It takes one argument:
		*iterables, which outputs list. This is arbitrary number of arguments
	1) First our function creates list object named res to whom it'll append future values
	2) Then our function creates minimum value of lengths of lists in our arguments using for loop inside min() function. It is for stopping zipping after seeing shortest iterable
	3) Our function creates for loop on range of minimum value and creates tuple of each iterable inside the iterables
	4) It appends that tuple into res list
	5) After all our function returns the list of tuples

	Example:
		result = my_zip([1, 2, 3], ['a', 'b', 'c'], ['x', 'y']) # here we see that our shortes iterable is "['x', 'y']". So after seeing this list, function should stop zipping.
		print(result)
	Output:
		[(1, 'a', 'x'), (2, 'b', 'y')]
	'''

	res = []
	min_length = min(len(it) for it in iterables)

	for i in range(min_length):
			tp = tuple(it[i] for it in iterables)
			res.append(tp)
	return res

result = my_zip([1, 2, 3], ['a', 'b', 'c'], ['x', 'y'])
print(result)
