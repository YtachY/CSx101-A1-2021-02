#!/usr/bin/env python3

a, b, c, d = [bool(int(i)) for i in input().split()]

result = bool((a ^ 1) * (b ^ 1) * (c ^ 1) + (a ^ 1) * (b ^ 1) * d + b * c)
print(int(result))