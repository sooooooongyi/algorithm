n=5
m=5
data=[1, 2, 3, 2, 5]

count=0
interval_sum=0
end=0

for start in range(n):
    while interval_sum<m and end<n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

#----------------------------------------------#
# start를 고정 시켜놓고 m을 넘어가지 않는 end를  #
# 찾음. 그 후로 start를 바깥 for문에서 하나씩 증 #
# 가 시키면서 찾음...!                          #
#----------------------------------------------#

print(count)