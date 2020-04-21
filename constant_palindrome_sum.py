num_test_cases  = int(input())

ns = []
ks = []
lists = []

for i in range(num_test_cases):
    s = input().split(" ")
    ns.append(int(s[0]))
    ks.append(int(s[1]))
    lists.append([int(s) for s in input().split(' ')])

for n, k, a in zip(ns, ks, lists):
    d = {}
     