#!/usr/bin/python3

def main():
	q = int(input())
	while (q):
		solve(int(input()))
		q -= 1

def solve(n):
	if (n == 2):
		print(2)
	else:
		if (n % 2 == 0):
			print(0)
		else:
			print(1)

if __name__ == "__main__":
	main()