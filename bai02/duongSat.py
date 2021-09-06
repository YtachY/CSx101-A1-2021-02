#!/usr/bin/python3

k, t = list(map(int, input().split()))

a = t // k
result = 0

if (a % 2 == 0):
	result = t % k
else:
	# print("k - t%k + 1", k, t)
	result = k - t % k

print(result)