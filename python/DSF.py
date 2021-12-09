from typing import Dict, Generic, TypeVar, Optional, Union

T = TypeVar('T')

class dsf(Generic[T]):
    def __init__(self, set: set[T]) -> None:
        self.set = set
        self.p: dict[T, Optional[T]] = {i: None for i in set} # initialize parent of each item to None (not in any set)
        self.rank: dict = {i: None for i in set} # initialize each rank to None (not in any set)
    
    def __repr__(self) -> str:
        sets = self.set_list()
        s = ''
        for i in sets.values():
            s += '{'
            for j in sets[i]:
                s += f'{j}, '
            s = s[:len(s)-2] + '} '
        return s

    

    # makes set in dsf
    def make_set(self, x) -> None:
        try:
            self.p[x] = x
            self.rank[x] = 0
        except KeyError:
            print('Error: indicated value not in dataset')

    # finds representative node of a set (i.e. the set the node is in)
    def find_set(self, x) -> Optional[T]:
        try:
            if x != self.p[x]:
                self.p[x] = self.find_set(self.p[x])
            return self.p[x]
        except KeyError:
            print('Error: indicated value not in dataset')

    # join 2 sets together
    def union(self, x: T, y: T) -> None:
        try:
            i = self.find_set(x)
            j = self.find_set(y)
            assert i is not None
            assert j is not None
            if self.rank[i] > self.rank[j]:
                self.p[j] = i
            else:
                self.p[i] = j
                if self.rank[i] == self.rank[j]:
                    self.rank[j] += 1
        except KeyError:
            print('Error: indicated value not in dataset')

    # makes dict of lists representing sets
    def set_list(self):
        sets = {}
        for i in self.rank.keys():
            if self.rank[i] != None:
                sets[i] = []
        for i in self.set:
            if self.find_set(i) != None:
                sets[self.find_set(i)].append(i)
        return sets

if __name__ == "__main__":
    s = {0, 1, 2, 3, 4, 6, 7}
    ds = dsf(s)
    print(ds)
    for i in s:
        ds.make_set(i)
    ds.union(7, 0)
    print(ds)
    ds.union(1, 3)
    ds.union(4, 6)
    ds.union(2, 6)
    print(ds)
    print(ds.rank)