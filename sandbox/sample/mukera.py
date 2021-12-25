

def xor(m, n):
	result = ''
	for x,y in zip(m, n):
		result += '0' if x == y else '1'
	return result


	