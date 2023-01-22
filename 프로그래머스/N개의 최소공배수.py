def solution(i, j):
	while i % j:
		i,j = j,i%j
	return j

print(solution(21, 14))