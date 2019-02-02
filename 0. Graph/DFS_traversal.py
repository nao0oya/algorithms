"""
DFS探索(深さ優先探索)
ルートノードで始まり隣接した全てのノードを探索する。それからこれらの最も近いノードのそれぞれに対して同様のことを繰り返して探索対象ノードをみつける。「横型探索」とも言われる。

"""
from collections import defaultdict

# 隣接する頂点をリストで表現する
class DFSOperator:

    def __init__(self):
        self.graph = defaultdict(list)
        self.output = []

    def addEdge(self, u: int, v: int):
        self.graph[u].append(v)

    # DFS探索関数
    def DFSUtil(self, v: int, visited: list):

        # 今の頂点を探索済みのリストに格納し、printする
        visited[v]= True
        self.output.append(v)

        # 今いる頂点に隣接する頂点を繰り返し探索する
        # this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # この関数はDFSUtilのラッパー関数で、
    # すべての頂点の数の分だけ探索済みリストのメモリを確保し、
    # 根頂点に隣接する頂点を再帰的にDFSUtil()を実行する
    def DFS(self):
        V = len(self.graph) #total vertices

        # すべての頂点分の探索済みリストのメモリを確保し、未探索状態で登録する
        visited =[False]*(V)

        # 再帰的に関数を呼び、初探索した頂点はprintする
        # DFSは一つの根ルート頂点から探索を開始する
        for i in range(V):
            if visited[i] == False:
                self.DFSUtil(i, visited)

