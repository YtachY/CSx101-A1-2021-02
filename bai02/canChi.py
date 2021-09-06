#!/usr/bin/python3


can = ["CANH", "TAN", "NHAM", "QUY", "GIAP", "AT", "BINH", "DINH", "MAU", "KY"]
chi = ["THAN", "DAU", "TUAT", "HOI", "TY'", "SUU", "DAN", "MAO", "THIN", "TY.", "NGO", "MUI"]

n = int(input())
if (n < 0):
	# print(n % 10)
	result = can[(n + 1) % 10 ] + ' ' + chi[(n + 1) % 12]
else:
	result = can[n % 10] + ' ' + chi[n % 12]

print(result)