import sys

def binary_search(ary, target):
    start = 0
    end = len(ary) - 1

    while True:
        if start > end: return -1
        mid = (start + end) // 2

        if mid > target: end = mid - 1
        elif mid < target: start = mid + 1
        else: return mid


num = int(sys.stdin.readline())
a, b, c, d = [], [], [], []

for i in range(num):
    e, f, g, h = map(int, sys.stdin.readline().split())
    a.append(e)
    b.append(f)
    c.append(g)
    d.append(h)

ab_list = []

for n1 in a:
    for n2 in b:
        ab_list.append(n1 + n2)
ab_list.sort()
answer = 0

for n1 in c:
    for n2 in d:
        target = -n1 -n2
        if binary_search(ab_list, target) != -1:
            answer += 1

print(answer)