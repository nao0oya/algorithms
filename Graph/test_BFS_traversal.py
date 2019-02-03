from collections import defaultdict
import unittest
from Graph.BFS_traversal import BFSOperator


class TestBFSOperator(unittest.TestCase):

    def setUp(self):
        self.BFS = BFSOperator()

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        self.BFS = None

    def testBFS(self):
        # グラフの準備
        g = self.BFS
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 2)
        g.addEdge(2, 0)
        g.addEdge(2, 3)
        g.addEdge(3, 3)

        # print ("BFT開始(頂点番号2からスタート)")
        g.traverseVertixs(2)

        self.assertListEqual([2,0,3,1], g.output)

if __name__ == "__main__":
    unittest.main()

