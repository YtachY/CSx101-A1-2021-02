#!/usr/bin/python3

a = float(input())
b = float(input())
c = float(input())

if (a < b + c and b < c + a and c < a + b):
	p = (a + b + c) / 2
	s = (p*(p-a)*(p-b)*(p-c)) ** 0.5
	if (s - int(s) == 0):
		s = int(s)
	if (a == b and b == c):
		print("Tam giac deu, dien tich = {}".format(round(s, 2)))
	elif (a == b or b == c or c == a):
		print("Tam giac can, dien tich = {}".format(round(s, 2)))
	elif ((a * a == b * b + c * c) or (a * a + b * b == c * c) or (a * a + c * c == b * b)):
		print("Tam giac vuong, dien tich = {}".format(round(s, 2)))
	else:
		print("Tam giac thuong, dien tich = {}".format(round(s, 2)))
else:
	print("Khong phai tam giac")