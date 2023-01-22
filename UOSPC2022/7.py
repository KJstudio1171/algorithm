import sys

A,B,L = map(int, sys.stdin.readline().rstrip().split())
bridge = []
ans = 0


for i in range(A):
	bridge.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(B):
	num1,num2 = map(int, sys.stdin.readline().rstrip().split())
	for j in bridge:
		if j[1] > 0 and num2 - abs(j[0] - num1) > 0:
			j[1] -= (num2 - abs(j[0] - num1))

for j in bridge:
	if j[1] > 0:
		ans = 1

if ans :
	print("NO")
else:
	print("YES")