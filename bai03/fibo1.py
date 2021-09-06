#!/usr/bin/env python3


# f = []
# f.append(0)
# f.append(1)
# for i in range(2, 50005):
# 	f.append(f[i - 1] + f[i - 2])

# n = int(input())
# print(f[n])

def f(n):
	if (n == 1):
		return 1
	elif (n == 2):
		return 1
	else:
		return f(n - 1) + f(n - 2)

def main():
	print(f(int(input())))

if __name__ == "__main__":
	main()