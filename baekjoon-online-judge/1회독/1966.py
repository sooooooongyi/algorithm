# 구현 - 프린터 큐
# Solution
# (1) 단순한 sorting 문제가 x -> 문제 이해 다시!
# (2) sorting을 하면 index 문제가 복잡해짐 -> index를 위한 list를 만들고, 삭제+삽입 과정을 같이함
# (숫자가 같아도 index에서 해당 값이 1이아니면, 처음에 지목한 그 숫자가 아님)

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    i_list = [0] * N
    i_list[M] = 1

    n_list = list(map(int, input().split()))
    cnt = 0

    while True:
        if n_list[0] == max(n_list):
            cnt += 1
            if i_list[0] == 1:
                print(cnt)
                break
            else:
                del n_list[0]
                del i_list[0]
        else:
            n_list.append(n_list[0])
            del n_list[0]
            i_list.append(n_list[0])
            del i_list[0]