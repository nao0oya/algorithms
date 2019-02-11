from Sort.insertion_sort import *
from Sort.bubble_sort import *
from Sort.selection_sort import *
from Sort.stable_sort import *

import unittest


class TestSort(unittest.TestCase):
    """
    :N: length of input list
    :A: input list
    """

    def test_sort_1(self):
        N = 1
        input_list = "100"
        A = list(map(int, input_list.split()))
        expect = [100]
        self.assertListEqual(expect, insertion_sort(A, N))
        self.assertListEqual(expect, bubble_sort(A, N))
        self.assertListEqual(expect, selection_sort(A, N))

    def test_sort_2(self):
        N = 6
        input_list = "5 2 4 6 1 3"
        A = list(map(int, input_list.split()))
        expect = [1, 2, 3, 4, 5, 6]
        self.assertListEqual(expect, insertion_sort(A, N))
        self.assertListEqual(expect, bubble_sort(A, N))
        self.assertListEqual(expect, selection_sort(A, N))

    def test_stable_sort(self):
        """
        compare with bubble sort and selection sort.
        In case, sort target number has suffix: trump suit, bubble sort is always stable.
        On the other hand, selection sort is sometimes not stable.
        [NOTE] S, H, C and D exprain hearts, diamonds, clubs and spades.
        """
        N = 5
        input_list = "H4 C9 S4 D2 C3"
        A = list(input_list.split())
        bubble_result, selection_result = stable_sort(A, N)
        self.assertListEqual(["D2", "C3", "H4", "S4", "C9"], bubble_result)
        self.assertListEqual(["D2", "C3", "S4", "H4", "C9"], selection_result)


