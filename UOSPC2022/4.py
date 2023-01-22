import sys

N,M = map(int, sys.stdin.readline().rstrip().split())
cost = 0
data = []
sum_data = 0

for i in range(M):
	num1, num2 = map(int, sys.stdin.readline().rstrip().split())
	sum_data += num1 + num2
	cost += num1
	data.append((num1, num2))

data.sort(reverse=True, key=lambda x : x[0])

n = True
while n :
	for i in data:
		if sum_data - i[0] - i[1] >= N:
			sum_data -= (i[0] + i[1])
			cost -= i[0]
			del i
			break
		n = False

print(cost)