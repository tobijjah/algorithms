from unittest import TestCase
from algorithms.disjointset import DisjointSetSimple


class TestDisjointSetSimple(TestCase):
    def setUp(self):
        self.djs = DisjointSetSimple()

    def test_make_set_create_consecutive_nodes(self):
        test_range = 100

        expected = list(range(1, test_range+1))
        actual = [self.djs.make_set() for i in range(test_range)]

        self.assertEqual(expected, actual, msg='Consecutive nodes violated.')

    def test_make_set_node_reference_itself(self):
        test_range = 100
        [self.djs.make_set() for i in range(test_range)]

        expected = list(range(1, test_range+1))
        actual = [self.djs.forest[node] for node in expected]

        self.assertEqual(expected, actual, msg='Self reference violated.')

    def test_path_compression(self):
        self.djs.forest = [0, 1, 1, 2, 3, 4, 5]
        self.djs._path_compression(6, 1)

        expected = [0, 1, 1, 1, 1, 1, 1]
        actual = self.djs.forest

        self.assertEqual(expected, actual, msg='Path compression failed')

    def test_find_root(self):
        self.djs.forest = [11, 1, 1, 2, 2, 1, 5, 6, 7, 7, 3, 3]

        expected = 1
        actual = self.djs._find(8)

        self.assertEqual(expected, actual, msg='Failed to find root')

    def test_union(self):
        pass

