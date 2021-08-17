h, b, c, s =map(int, input().split())
result = h*b*c*s
print("%.1f MB" %(result/8/1024/1024))