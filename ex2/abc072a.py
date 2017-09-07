'''
X, t = map(int, input().split())

if X <= t:
    ans = 0
else:
    ans = X - t
print(ans)

s = input()
line = s[::2]
print(line)

from collections import Counter
N = int(input())

a = list(map(int, input().split()))
que = []

for i in range(N):
    num = a[i]
    que.append(num+1)
    que.append(num)
    que.append(num-1)


counter = Counter(que)
for word, cnt in counter.most_common(1):
    print(cnt)
'''

import sys
sys.setrecursionlimit(10000)

N = int(input())
p = list(map(int, input().split()))

def solve(i, c):
    if i == N - 1:
        return c
    if p[i] == i+1:
        a = p[i]
        p[i] = p[i+1]
        p[i+1] = a
        c += 1
    return solve(i+1, c)

print(solve(0, 0))
