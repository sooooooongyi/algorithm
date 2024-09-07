# 🌜, ✨ sort인데 등수를 따져야하는..!

n, score, p = map(int, input().split())
scores = []

if n != 0:
    scores = list(map(int, input().split()))

scores.append(score)
scores.sort(reverse=True)
scoreIdx = scores.index(score)
cntScore = scores.count(score)

if scoreIdx + (cntScore-1) > p-1:
    print(-1)
else:
    print(scoreIdx+1)