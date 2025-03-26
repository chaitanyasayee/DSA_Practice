import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm to create a MST (Minimum Spanning Tree)
        n = len(points)
        total_cost = 0
        heap = [(0, 0)]
        seen = set()

        while len(seen) < n:
            dist, i = heapq.heappop(heap)
            if i in seen:
                continue
            
            seen.add(i)
            total_cost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    nei_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(heap, (nei_dist, j))
        
        return total_cost
                    