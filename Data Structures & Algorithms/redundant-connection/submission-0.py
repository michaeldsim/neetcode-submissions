class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(len(edges))]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_y != root_x:
                parent[root_y] = root_x
                return False
            else:
                return True
        
        for x, y in edges:
            res = union(x - 1, y - 1)

            if res:
                return [x, y]