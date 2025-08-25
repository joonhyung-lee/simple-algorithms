def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	m = len(b)
	res: list[int|float] = []
 
	for row in a:
		if len(row) != m:
			return -1
		acc = 0
		for i in range(m):
			acc += row[i] * b[i]
		res.append(acc)
	return res