# 세그멘테이션 트리 - 최솟값과 최댓값
# Solution
# (1) 일단 기본적 트리공부를 다시하자..

n, m = map(int, input())
arr = [0]*(n+1)
tree_min = [0]*(n+1)*4
tree_max = [0]*(n+1)*4

def init_min(start, end, node):
    if start==end:
        tree_min[start]=arr[start]
        return tree_min[node]
    mid = (start+end)//2
    tree_min[node] = min(init_min(node*2, start, mid), init_min(node*2+1, mid+1, end))
    return tree_min[node]

def init_max(start, end, node):
    if start==end:
        tree_max[start]=arr[start]
        return tree_max[node]
    mid = (start+end)//2
    tree_max[node] = max(init_max(node*2, start, mid), init_max(node*2+1, mid+1, end))
    return tree_max[node]

def search_min(node, start, end, left, right):
    if start > right or end < left:
        return 1e9
    if left <= start and end <= right:
        return tree_min[node]
    mid = (start + end)//2
    return min(search_min(node*2, start, mid, left, right), search_min(node*2+1, mid+1, end, left, right))

def search_max(node, start, end, left, right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return tree_max[node]
    mid = (start + end)//2
    return max(search_max(node*2, start, mid, left, right), search_max(node*2+1, mid+1, end, left, right))

init_min(1, 0, n-1)
init_max(1, 0, n-1)

for _ in range(m):
    a, b = [int(x) for x in sys.stdin.readline().split()]

    print(search_min(1, 0, n-1, a-1, b-1), end = ' ')
    print(search_max(1, 0, n-1, a-1, b-1))