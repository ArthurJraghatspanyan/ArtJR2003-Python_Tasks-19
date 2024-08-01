#  Create a function named get_nth_element that takes an iterable and an integer n, and returns the n-th element from the iterable using iter() and next().

def get_nth_element(iterable, n):
	it = iter(iterable)
	nth_element = next(it)

	for i in range(len(iterable)):
		if n == i:
			nth_element = iterable[i]

	return nth_element

ls = [1, 2, 3, 4, 5]
result = get_nth_element(ls, 3)
print(result)
