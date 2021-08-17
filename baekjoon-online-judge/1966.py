# 구현 - 프린터 큐
# Solution
# (1) 단순한 sorting 문제가 x -> 문제 이해 다시!
# (2) sorting을 하면 index 문제가 복잡해짐 -> index를 위한 list를 만들고, 삭제+삽입 과정을 같이함
# (숫자가 같아도 index에서 해당 값이 1이아니면, 처음에 지목한 그 숫자가 아님)

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    i_list = [0 for _ in range(N)]
    i_list[M] = 1
    count = 0
    p_list = list(map(int, input().split()))

    while True: 
        if p_list[0] == max(p_list):
            count += 1
            if i_list[0] == 1:
                print(count)
                break
            else:
                del p_list[0]
                del i_list[0]
        else:
            p_list.append(p_list[0])
            del p_list[0]
            i_list.append(i_list[0])
            del i_list[0]