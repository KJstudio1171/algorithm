import sys

N = int(sys.stdin.readline().rstrip())

num_list = []

for i in range(N):
	num_list.append(int(sys.stdin.readline().rstrip()))

max_data = max(num_list)
sum_data = sum(num_list)

size = 0
while size < sum_data :
	size += max_data

print(size)