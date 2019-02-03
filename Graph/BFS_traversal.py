"""
BFS (Breadth First Search) 幅優先探索
BFS()の引数で渡された箇所を起点として探索可能な頂点を探し、すべての頂点を探索する。
"""
from collections import defaultdict

class BFSOperator:

    output = []

    def __init__(self):
        """
        グラフはvalueをlist型で持つDictを用意
        """
        self.graph = defaultdict(list)

    def addEdge(self, u: int, v: int):
        """
        グラフの頂点を追加する
        """
        self.graph[u].append(v)

    def traverseVertixs(self, s):
        """
        BDSで各探索段階で発見した頂点の値を順番にprintする
        """
        # 頂点の探索状態を表現するlistを作成
        visited = [False] * (len(self.graph))

        # キューの作成
        queue = []

        # 現在の頂点をキューに格納(一番最初は引数で渡された番号の頂点)
        # 現在の頂点の探索履歴をTrueにする
        queue.append(s)
        visited[s] = True

        # キューの中身が空の状態になるまでループする
        while queue:

            # キューの中から0番目を抜き出す
            # 抜き出した値をprintする
            s = queue.pop(0)
            # print(s, end=" ")
            self.output.append(s)

            # 現在の頂点に隣接するすべての頂点の番号を取得する
            # 取得した頂点番号が未探索だった場合、キューに格納する
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

