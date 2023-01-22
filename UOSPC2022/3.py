import sys

Q,K = map(int, sys.stdin.readline().rstrip().split())

sum_d = 0
d1 = []
d2 = []

for i in range(Q):
	num1, num2 = map(int, sys.stdin.readline().rstrip().split())
	sum_d += num1
	if num2 == 0:
		d1.append(sum_d)
	else:
		d2.append(sum_d)
print((K - min(d2)),(K - max(d1) - 1))