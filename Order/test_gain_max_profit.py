from collections import defaultdict
import unittest
from Order.gain_max_profit import GainMaxProfit


class TestGainMaxProfit(unittest.TestCase):

    def setUp(self):
        self.executor = GainMaxProfit()

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        self.executor = None

    def testBase(self):
        R = [6, 5, 3, 1, 3, 4, 3]

        actual = self.executor.main(R)
        # print ("BFT開始(頂点番号2からスタート)")
        
        self.assertEqual(3, actual)

if __name__ == "__main__":
    unittest.main()

