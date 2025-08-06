class SegmentTree:
    def __init__(self, arr):
        n = len(arr)
        self.n = n
        self.tree = [0] * 4*n
        self._build(arr, 1, 0, n-1)
    
    def _build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
            return
        m = (l+r) // 2
        self._build(arr,node*2, l, m)
        self._build(arr, node*2+1, m+1, r)
        self.tree[node] = max(self.tree[node*2], self.tree[node*2+1])
    
    def query(self, L, R, node=1, l=0, r=None):
        if r is None: r = self.n - 1
        if R < l or L > r: return float('-inf')
        if L <= l and r <= R: return self.tree[node]
        m = (l+r) // 2
        return max(
            self.query(L, R, node*2, l, m),
            self.query(L, R, node*2+1, m+1, r)
        )
    
    def update(self, idx, val, node=1, l=0, r=None):
        if r is None: r = self.n - 1
        if l==r:
            self.tree[node] = val
            return
        m = (l+r) // 2
        if idx <= m:
            self.update(idx, val, node*2, l, m)
        else:
            self.update(idx, val, node*2+1, m+1, r)
        self.tree[node] = max(self.tree[node*2], self.tree[node*2+1])
    
    def find_first_and_update(self, node, l, r, x):
        # if max in current segment smaller than x, no basket can hold the fruit
        if self.tree[node] < x:
            return -1
        
        if l==r:
            # leaf node, suitable basket found, mark as used
            self.tree[node] = 0
            return l
        
        m = (l+r) // 2
        
        # try left child first
        res = self.find_first_and_update(node*2, l, m, x)
        if res==-1:
            # try right if left failed
            res = self.find_first_and_update(node*2+1, m+1, r, x)
        
        # update current node after child is updated
        self.tree[node] = max(self.tree[node*2], self.tree[node*2+1])
        return res

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        seg = SegmentTree(baskets)
        unplaced = 0

        for fruit in fruits:
            idx = seg.find_first_and_update(1, 0, n-1, fruit)
            if idx==-1:
                unplaced += 1
        
        return unplaced