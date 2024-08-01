#Write a Python script that manually iterates over a list of numbers using the iter() and next() functions. This task will help you understand how Python handles iteration behind the scenes.

ls = [1, 2, 3, 4, 5]
it = iter(ls)
while True:
	if not it:
		break
	number = next(it, None)
	if number is None:
		break
	print(number)
