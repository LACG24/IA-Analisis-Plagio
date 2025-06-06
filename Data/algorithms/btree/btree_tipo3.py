class BTreeNode:
    
    
    
    
        if i < len(self.keys) and self.keys[i] == k:
            return self

        if self.leaf:
            return None

        return self.children[i].search(k)


class BTree:
    
    
    
    
    
    
        if not y.leaf:
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    
# Example usage:
if __name__ == "__main__":
    btree = BTree(3)  # Create a B-tree with minimum degree 3
    btree.insert(10)
    btree.insert(20)
    btree.insert(5)
    btree.insert(6)
    btree.insert(12)
    btree.insert(30)
    btree.insert(7)
    btree.insert(17)

    print("Traversal of the BTree:")
    btree.traverse()  # Output the tree keys in sorted order
    print("\nSearching for key 6 in the tree:")
    result = btree.search(6)
    print(f"Key {6} found: {result is not None}")

def insert_non_full(self, nodo, k):
        """
        Insert a key `k` into a non-full nodo.
        """
        i = len(nodo.keys) - 1
        if nodo.leaf:
            nodo.keys.append(None)
            while i >= 0 and k < nodo.keys[i]:
                nodo.keys[i + 1] = nodo.keys[i]
                i -= 1
            nodo.keys[i + 1] = k
        else:
            while i >= 0 and k < nodo.keys[i]:
                i -= 1
            i += 1
            if len(nodo.children[i].keys) == 2 * self.t - 1:
                self.split_child(nodo, i)
                if k > nodo.keys[i]:
                    i += 1
            self.insert_non_full(nodo.children[i], k)


def split_child(self, parent, i):
        """
        Split the child `i` of `parent` nodo.
        """
        t = self.t
        y = parent.children[i]
        z = BTreeNode(t, y.leaf)
        parent.children.insert(i + 1, z)
        parent.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t - 1)]
        y.keys = y.keys[0:(t - 1)]


def insert(self, k):
        """
        Insert a key `k` into the BTree.
        """
        if self.root is None:
            self.root = BTreeNode(self.t, leaf=True)
            self.root.keys = [k]
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                s = BTreeNode(self.t, leaf=False)
                s.children.insert(0, self.root)
                self.split_child(s, 0)
                i = 0
                if s.keys[0] < k:
                    i += 1
                self.insert_non_full(s.children[i], k)
                self.root = s
            else:
                self.insert_non_full(self.root, k)


def search(self, k):
        """
        Search for a key `k` in the BTree.
        """
        if self.root is not None:
            return self.root.search(k)
        return None


def traverse(self):
        """
        Traverses the whole tree.
        """
        if self.root is not None:
            self.root.traverse()


def __str__(self):
        """Visualize the whole tree structure for easier debugging."""
        if self.root is not None:
            return str(self.root)
        return "Empty Tree"


def __init__(self, t):
        """
        Initialize a BTree with the minimum degree `t`.
        """
        self.root = None
        self.t = t  # Minimum degree


def search(self, k):
        """
        Search for a key in the subtree rooted with this nodo.
        """
        i = 0
        while i < len(self.keys) and k > self.keys[i]:
            i += 1


def traverse(self):
        """
        Traverses all nodes in a subtree rooted with this nodo and prints the keys.
        """
        for i in range(len(self.keys)):
            if not self.leaf:
                self.children[i].traverse()
            print(self.keys[i], fin=" ")
        if not self.leaf:
            self.children[len(self.keys)].traverse()


def __str__(self):
        """Visualize the nodo structure for easier debugging."""
        return f"Keys: {self.keys}, Leaf: {self.leaf}"


def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.keys = []  # List of keys
        self.children = []  # List of child pointers
        self.leaf = leaf  # Boolean to indicate if the nodo is a leaf
