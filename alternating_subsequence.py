num_test_cases  = int(input())

ns = []
lists = []

for i in range(num_test_cases):
    ns.append(int(input()))
    lists.append([int(s) for s in input().split(' ')])

for n, a in zip(ns, lists):
    b = [a[0]]
    for ai in a[1:]:
        if ai * b[-1] > 0:
            b[-1] = max(ai, b[-1])
        else:
            b.append(ai)
    print(sum(b))