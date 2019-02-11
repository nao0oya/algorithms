
def trace(A: list):
    print(*A)

def selection_sort(A: list, N:int) -> list:
    """
    :A[N]: サイズがNの整数型配列。
    :i: 未ソートの部分の先頭を指すループ変数で、配列の先頭から末尾に向かって移動する。
    :minj: 各ループの処理でi 番目からN-1 番目までの要素で最小のものの位置。j 未ソートの部分から最小値の位置（minj）を探すためのループ変数。
    """
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        # alter position
        if i != minj:
            a, b = A[i], A[minj]
            A[i], A[minj] = b, a

    return A

