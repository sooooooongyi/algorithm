# 🌜, ✨ 사용되는 단어 집 만들기 + 집에 갯수 넣기

s = input().upper()
sList = list(set(s)) # 중복 없는 진짜 알파벳 개수
cntList = []

for i in sList:
    cnt = s.count(i)
    cntList.append(cnt)
    
if cntList.count(max(cntList)) > 1:
    print('?')
else: 
    print(sList[cntList.index(max(cntList))])