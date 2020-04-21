ns = [int(input()) for i in range(int(input()))]

for n in ns:

    k = 2
    s = 3

    while True:
        if n % s == 0:
            x = int(n / s)
            print(x)
            break
        else:
            k += 1
            s += 2 ** (k - 1)