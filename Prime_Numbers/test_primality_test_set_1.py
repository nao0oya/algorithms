from collections import defaultdict
import unittest
from Prime_Numbers.primality_test_set_1 import PrimalityTester1


class TestPrimalityTester1(unittest.TestCase):

    def setUp(self):
        self.TPD = PrimalityTester1()

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        self.TPD = None

    def test_is_prime(self):
        not_prime = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36]
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        
        for i in range(len(not_prime)):
            self.assertFalse(self.TPD.is_prime(not_prime[i]))
            
        for i in range(len(prime)):
            self.assertTrue(self.TPD.is_prime(prime[i]))


if __name__ == "__main__":
    unittest.main()

