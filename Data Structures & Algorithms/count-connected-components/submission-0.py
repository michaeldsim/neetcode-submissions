class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                parent[root_y] = root_x

        for x, y in edges:
            union(x, y)
        
        roots = set([find(i) for i in range(n)])

        return len(roots)