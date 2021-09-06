#!/usr/bin/env python3

def main():
	# with open("inp.txt", "r") as f:
	# 	inp = [int(i) for i in f.read().split()]


	# doi1 = [inp[:3], inp[3:6], inp[6:9]]
	# print(doi1)
	# doi2 = [inp[-9:-6], inp[-6:-3], inp[-3:]]
	# print(doi2)

	doi1 = [[int(i) for i in input().split()],
         [int(i) for i in input().split()],
         [int(i) for i in input().split()]]
	doi2 = [[int(i) for i in input().split()],
         [int(i) for i in input().split()],
         [int(i) for i in input().split()]]
	a = solve(doi1)
	b = solve(doi2)
	for i in range(3):
		if (a[i] > b[i]):
			print(' '.join(map(str,(a))))
			exit()
		elif (a[i] < b[i]):
			print(' '.join(map(str,(b))))
			exit()
	if (a[4] >= b[4]):
		print(' '.join(map(str, (b))))
	else:
		print(' '.join(map(str,(a))))

def solve(a):
	diem = 0
	hieuSo = 0
	banThang = 0
	fairPlay = 0
	for i in range(len(a)):
		banThang += a[i][0]
		hieuSo += a[i][0] - a[i][1]
		fairPlay += a[i][2]
		if (a[i][0] > a[i][1]):
			diem += 3
		elif (a[i][0] == a[i][1]):
			diem += 1
	return [diem, hieuSo, banThang, fairPlay]

if __name__ == "__main__":
	main()
