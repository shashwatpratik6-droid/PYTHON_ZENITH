import math

x = int(input())
h = []
for i in range(1, x + 1):
    l, a, b = map(int, input().split())
    g = math.gcd(b, l)
    ans = (l - 1) - ((l - 1 - a) % g)
    h.append(ans)

for k in range(0, len(h)):
    print(h[k])