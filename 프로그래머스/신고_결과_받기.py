def solution(id_list, report, k):
	answer = []
	report_list = {string:set() for string in id_list}
	answer_list = {string:0 for string in id_list}

	for string in report:
		(a,b) = string.split(" ")
		report_list[b].add(a)
	for key in report_list:
		if(len(report_list[key]) >= k):
			for i in report_list[key]:
				answer_list[i] += 1
	for string in id_list:
		answer.append(answer_list[string])
	return answer
	

	

solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)