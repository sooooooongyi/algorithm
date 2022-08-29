h, m = map(int, input().split())
c = int(input())

h = (h + (m+c)//60)%24
m = (m+c)%60

print(str(h)+" "+str(m))
