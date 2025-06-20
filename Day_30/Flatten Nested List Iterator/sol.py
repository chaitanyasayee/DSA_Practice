class NestedIterator: # not working if memory is limited and input is huge list
    def __init__(self, nestedList: [NestedInteger]):
        def dfs(nestedList):
            for e in nestedList:
                if e.isInteger():
                    self.vals.append(e.getInteger())
                else:
                    dfs(e.getList())

        self.vals = []
        dfs(nestedList)
        self.cur = 0

    def next(self) -> int:
        res = self.vals[self.cur]
        self.cur += 1
        return res

    def hasNext(self) -> bool:
        return self.cur < len(self.vals)
