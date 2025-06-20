class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        rep = 0
        opened= set()
        hk = set()
        seen = set(initialBoxes)
        q = deque(initialBoxes)
        while q:
            box = q.popleft()
            if (status[box] == 0 and not box in hk) or (box in opened): 
                continue
            opened.add(box)
            rep += candies[box]

            for x in keys[box]:
                hk.add(x)
                if x in seen and not x in opened: q.append(x)
            for c in containedBoxes[box]:
                if not c in seen:
                    seen.add(c)
                    q.append(c)

        return rep
        