from collections import defaultdict
import unittest
from DFS_traversal import DFSOperator


class TestDFSOperator(unittest.TestCase):

    def setUp(self):
        self.DFS = DFSOperator()

    # テストメソッドの実行が終わるたびに呼ばれる
    def tearDown(self):
        self.DFS = None

    def testDFS(self):
        # グラフの準備
        g = self.DFS
        g.addEdge(2, 0)
        g.addEdge(0, 1)
        g.addEdge(0, 2)
        g.addEdge(1, 2)
        g.addEdge(2, 3)
        g.addEdge(3, 3)

        g.DFS()

        self.assertListEqual([0,1,2,3], g.output)

if __name__ == "__main__":
    unittest.main()

