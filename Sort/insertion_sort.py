
def trace(A: list):
    print(*A)

def insertion_sort(A: list, N:int) -> list:
    """
    A[N]: サイズがNの整数型配列。
    i: 未ソートの部分列の先頭を示すループ変数。
    v: A[i]の値を一時的に保持しておくための変数。
    j: ソート済み部分列からvを挿入するための位置を探すループ変数。
    """
    for i in range(1, N):
        v = A[i]
        j = i - 1
        while j >= 0 and v < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        # trace(A)

    return A
