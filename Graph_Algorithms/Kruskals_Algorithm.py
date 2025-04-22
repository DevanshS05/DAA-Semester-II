class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(self.heap)

        if left < n and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left
        if right < n and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_min_heap(self, arr):
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(i)

    def insert(self, weight, vertex_pair):
        self.heap.append((weight, vertex_pair))
        i = len(self.heap) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] < self.heap[parent][0]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def is_empty(self):
        return len(self.heap) == 0


# Disjoint Set (Union-Find)
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu != pv:
            self.parent[pu] = pv
            return True
        return False


# Kruskal's Algorithm
def kruskal(n, edges):
    heap = MinHeap()
    heap.build_min_heap(edges)

    ds = DisjointSet(n)
    mst = []
    mst_cost = 0

    while not heap.is_empty() and len(mst) < n - 1:
        weight, (u, v) = heap.extract_min()
        if ds.union(u, v):
            mst.append((u, v, weight))
            mst_cost += weight

    return mst, mst_cost


# Driver Code

n = 5  # Number of vertices
edge_list = [
    (10, (0, 1)),
    (6, (0, 2)),
    (5, (0, 3)),
    (15, (1, 3)),
    (4, (2, 3)),
    (2, (1, 2)),
    (8, (3, 4))
]

mst, cost = kruskal(n, edge_list)
print("Edges in MST:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")
print("Total cost of MST:", cost)
