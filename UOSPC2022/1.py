import sys

num1, num2, num3 = map(int, sys.stdin.readline().rstrip().split())

if (num1 * num3) > num2:
	print("NO")
else:
	print("YES")