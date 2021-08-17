num = input()
index = 10000
for i in range(len(num)):
    print("["+str(int(num[i])*index)+"]")
    index = int(index/10)
