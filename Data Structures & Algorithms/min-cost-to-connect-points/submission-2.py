class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = [x for x in range(len(points))]
        rank = [1] * len(points)
        costs = []
        self.unions = 0
        res = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if rank[root_x] < rank[root_y]:
                    root_x, root_y = root_y, root_x

                parent[root_y] = root_x
                rank[root_x] += rank[root_y]
                self.unions += 1
                return True
    
            return False
        
        def calculate_manhattan_distance(point1, point2):
            xi, yi = point1
            xj, yj = point2

            return abs(xi - xj) + abs(yi - yj)

        for point1_idx in range(len(points)):
            for point2_idx in range(point1_idx + 1, len(points)):
                if point2_idx != point1_idx:
                    point1 = points[point1_idx]
                    point2 = points[point2_idx]

                    costs.append((calculate_manhattan_distance(point1, point2), point1_idx, point2_idx))
        
        costs.sort()

        for cost, point1_idx, point2_idx in costs:
            if union(point1_idx, point2_idx):
                res += cost
                if self.unions == len(points) - 1:
                    break
        
        return res
