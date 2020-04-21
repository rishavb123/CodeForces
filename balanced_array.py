ns = [int(input()) for i in range(int(input()))]

for n in ns:
    if n % 4 != 0:
        print("NO")
        continue
    print("YES")
    a = []
    b = []
    for i in range(1, int(n / 2) + 1):
        a.append(str(i * 2))
        b.append(str(i * 2 - 1))
    b[-1] = str(int(b[-1]) + int(n / 2))
    print(' '.join(a + b))