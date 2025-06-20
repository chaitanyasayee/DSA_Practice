class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x1,x2,y1,y2 = 0,0,0,0
        max_distance = 0
        for loc,dis in enumerate(s):
            if dis == 'N':
                y1+=1
            elif dis == 'S':
                y2+=1
            elif dis == 'E':
                x1+=1
            else:
                x2+=1
            coverd = loc +1
            conflicts = min(x1,x2) + min(y1,y2)
            if k>= conflicts:
                coverd_distance = coverd
            else:
                distance = coverd - 2*conflicts
                coverd_distance = distance +2*k
            max_distance = max(max_distance, coverd_distance)
        return max_distance