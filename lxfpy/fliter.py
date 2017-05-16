def is_palindrome(n):
	nreverse = int(str(n)[::-1])
	return n == nagainst

if __name__ == '__main__':
	output = filter(is_palindrome, range(1, 1000))
	print(list(output))