#!/usr/bin/python3

from math import gcd

def main():
	t = int(input())
	while (t):
		a, b = list(map(int, input().split()))
		rutgon(a, b)
		t -= 1


def rutgon(x, y):
	d = gcd(x, y);

	x = x // d;
	y = y // d;
	if (y != 1):
		print(f"{x} {y}");
	else:
		print(x);


main()