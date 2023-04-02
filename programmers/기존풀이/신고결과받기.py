from collections import defaultdict

def solution(id_list, report, k):
  answer = [0] * len(id_list)

  report = set(report)
  report_dic = defaultdict(set)
  report_count = defaultdict(int)

  reported_list = []

  for r in report:
    reporter, reported = r.split()
    report_count[reported] += 1
    report_dic[reporter].add(reported)

    if report_count[reported] == k:
      reported_list.append(reported)

  for s in reported_list:
    for i in range(len(id_list)):
      if s in report_dic[id_list[i]]:
        answer[i] += 1

  return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))