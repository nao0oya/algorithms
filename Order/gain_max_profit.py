"""
ADLS1_1
最大の利益
FX取引では、異なる国の通貨を交換することで為替差の利益を得ることができます。例えば、１ドル100円の時に 1000ドル買い、価格変動により 1ドル 108円になった時に売ると、(108円 − 100円) × 1000ドル = 8000円の利益を得ることができます。

ある通貨について、時刻 t における価格 Rt (t=0,1,2,,,n−1)が入力として与えられるので、価格の差 Rj−Ri (ただし、j>i とする) の最大値を求めてください。

入力
最初の行に整数 n が与えられます。続く n 行に整数 Rt (t=0,1,2,,,n−1) が順番に与えられます。

出力
最大値を１行に出力してください。

制約
2≤n≤200,000
1≤Rt≤109
入力例 1
6
5
3
1
3
4
3
入力例 1 に対する出力
3
入力例 2
3
4
3
2
入力例 2 に対する出力
-1
Note
Algorithm 
Source: https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_1_D
"""
from collections import defaultdict


class GainMaxProfit:

    def __init__(self):
        pass

    def main(self, input: list) -> int:
        R = input
        minv = R[0]
        max_diff = -20000000
        for i in range(1, len(R)):
            max_diff = max(max_diff, R[i] - minv)
            minv = min(minv, R[i])
        return max_diff