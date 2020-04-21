num_test_cases  = 1# int(input())

outputs = []

def find(visited, current, target, edges):
    if current == target: return []
    paths = []
    for edge in edges:
        if edge[0] == current and edge[1] not in visited:
            f = find(visited + [edge[1]], edge[1], target, edges)
            if f is not None:
                paths.append(f)
    if len(paths) == 0: return None
    path = min(paths, key=len)
    return path
        

for _ in range(num_test_cases):
    n, m, a, b, c = [int(x) for x in input().split(" ")]
    p = [int(x) for x in input().split(" ")]
    edges = []
    for _ in range(m):
        s = input().split(" ")
        edges.append((int(s[0]), int(s[1])))
        edges.append((int(s[1]), int(s[0])))
        
    total_path = find([], a, b, edges) + find([], b, c, edges)

for o in outputs: print(o)