# 🌜 (1) 팀별로 6명이 되는지 조건 (2) 등수 별로 점수
# ✨ 4등까지, 점수가 동일하면 5등 비교조건이 있어서, 등수를 항상 가지고 다녀야함..!

import sys 
input = sys.stdin.readline

t = int(input())

for i in range(t):
	n = int(input())
	team = list(map(int, input().strip().split()))

	manage = {}
	for j in range(n):
		if team[j] not in manage:
			# 팀 명수, 선수들 점수리스트, 점수합계
			manage[team[j]] = [1, [], 0]
		else:
			manage[team[j]][0] += 1

	# 선수들의 수가 조건에 맞지 않는 팀을 우선걸러낸다
	contain = set(k for k, v in manage.items() if v[0] < 6)

	grade = 1
	for j in range(n):
		# 점수계산에서 제외해야 하는 선수가 아니라면
		if team[j] not in contain:
			manage[team[j]][1].append(grade)
			# 점수를 더하는건 상위 4명의 점수까지만 합산
			if len(manage[team[j]][1]) <= 4: 
				manage[team[j]][2] += grade
			grade += 1



	answer = []
	for k, v in manage.items():
		if len(v[1]) != 0 and v[2] != 0:
			answer.append([k, v[1][4], v[2]])

	a = sorted(answer, key = lambda x : (x[2], x[1]))
	print(a[0][0])