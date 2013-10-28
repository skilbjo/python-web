def outer():
	outer.y = 0
	def inner():
		outer.y += 1
		return outer.y
	return inner

f = outer()

print(f(), f(), f())