#!/usr/bin/env python3
# int n,m,x,y,k,ans,dxl,dxr,dyl,dyr,drx0,drx1,dry0,dry1;


def analysis(n, m, x, y, k):
	if (k == 1):
		return 0
	if (n < k):
		if (m == k):
			return k-1
		if(y==1 or y==m):
			return k-1
		else:
			return k

	if ((x==1 or x==n) and (y==1 or y==m)):
		return k;
	if (x==1 or x==n or y==1 or y==m):
		if (y == 1 or y == m):
			n, m = m, n
			x, y = y, x
		return k + (y >= k and (m - y + 1) >= k);

	drx0 = n > k;
	drx1 = n >= k;
	dxl = (n - x + 1) >= k;
	dxr = x >= k;
	dry0 = m > k;
	dry1 = m >= k;
	dyl = (m - y + 1) >= k;
	dyr = y >= k;
	return k - 1 + min(drx0+dry1+dyl*dyr, dry0+drx1+dxl* dxr);


def main():
	# with open("inp.txt", "r") as f:
	# 	n, m, x, y, k = list(map(int, f.read().split()))
	
	n, m = list(map(int, input().split()))
	x, y = list(map(int, input().split()))
	k = int(input())
	if (n > m):
		n, m = m, n
		x, y = y, x
	ans = analysis(n, m, x, y, k)
	print(ans)
	return 0

if __name__ == "__main__":
	main()