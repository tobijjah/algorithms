from abc import ABCMeta, abstractmethod


__all__ = [
    'DisjointSetSimple',
    'DisjointSet',
]


class DisjointSetBase(metaclass=ABCMeta):
    """
    Base class for several implementations of the
    Union-find algorithm/Disjoint-set data structure.

    Source: Galler, Bernard A. and Fischer, Michael J.,
    "An improved equivalence algorithm",
    Communications of the ACM, no. 7, 1964
    """
    def __init__(self, forest):
        self.forest = forest

    @abstractmethod
    def make_set(self, data):
        pass

    @abstractmethod
    def union(self, x, y):
        pass

    @abstractmethod
    def _find(self, node):
        pass

    @abstractmethod
    def _path_compression(self, node, root):
        pass


class DisjointSetSimple(DisjointSetBase):
    def __init__(self):
        super().__init__([0])
        self.rank = [0]

    def make_set(self, data=None):
        """
        Creates consecutive self referencing nodes.
        Solution adapted from:
        https://www.ocf.berkeley.edu/~fricke/projects/hoshenkopelman/hk.c

        :return: int
            A node referencing itself.
            e.g. self.forest[i] = i
        """
        self.forest[0] += 1
        self.forest.append(self.forest[0])
        self.rank.append(0)

        return self.forest[0]

    def union(self, node1, node2):
        node1_root = self._find(node1)
        node2_root = self._find(node2)

        if node1_root == node2_root:
            return

        if (self.rank[node1_root] > self.rank[node2_root]
                or self.rank[node1_root] == self.rank[node2_root]):

            self.rank[node1_root] += 1
            self.rank[node2_root] = 0
            self.forest[node2_root] = node1_root

        else:
            self.rank[node2_root] += 1
            self.rank[node1_root] = 0
            self.forest[node1_root] = node2_root

    def _find(self, node):
        """

        :param node: int
        :return: int
        """
        if node > len(self):
            raise ValueError('Unknown node %s.' % node)

        root = node

        while self.forest[root] != root:
            root = self.forest[root]

        self._path_compression(node, root)

        return root

    def _path_compression(self, node, root):
        while self.forest[node] != node:
            self.forest[node], node = root, self.forest[node]

    def __len__(self):
        return self.forest[0]


class DisjointSet(DisjointSetBase):
    def __init__(self):
        super().__init__({})

    def make_set(self, data):
        node = _Node(rank=0, data=data)
        self.forest[data] = node

    def union(self, data1, data2):
        node1 = self._find(node=self._get_node(data1))
        node2 = self._find(node=self._get_node(data2))

        if node1 == node2:
            return

        if node1.rank > node2.rank or node1.rank == node2.rank:
            node1.rank += 1
            node2.rank = 0
            node2.parent = node1

        else:
            node2.rank += 1
            node1.rank = 0
            node1.parent = node2

    def _find(self, node):
        root = node

        while root.parent != root:
            root = root.parent

        self._path_compression(node=node, root=root)

        return root

    def _get_node(self, data):
        if data in self.forest:
            return self.forest[data]

        raise ValueError('No node for data %s' % data)

    def _path_compression(self, node, root):
        while node.parent != node:
            node.parent, node = root, node.parent

    def __len__(self):
        return len(self.forest)


class _Node:
    __slots__ = 'parent', 'rank', 'container'

    def __init__(self, rank, data):
        self.parent = self
        self.rank = rank
        self.container = data

    def __repr__(self):
        return 'Node<{}>({}, {}) Parent<{}>'.format(
            self.__hash__(),
            self.rank,
            self.container,
            self.parent.__hash__()
        )


if __name__ == '__main__':
    djs = DisjointSetSimple()
    djs.make_set()
    djs.make_set()
    djs.make_set()
    djs.make_set()
    djs.make_set()
    djs.union(1, 2)
    djs.union(2, 3)
    djs.union(4, 5)
    djs.union(4, 3)
    print(djs.forest)
