def hola(n):
	result = 1
	for x in range(1, n+1):
		result *= x 

	return result


print(hola(5))
print(hola(3))
print(hola(8))
print(hola(1))
