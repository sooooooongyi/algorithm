arr = input().split()
for i in arr:
    if (int(i)>0):
        print("plus")
    else:
        print("minus")
    if int(i)%2==0:
        print("even")
    else:
        print("odd")