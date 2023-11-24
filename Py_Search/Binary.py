def binSearch(A: list, elem: int) -> list:
    # если искомый элемент за границами диапазона,то делать нечего
    if elem > max(A) or elem < min(A):
        return [None]

    # определим верхнюю границу и вызовем рекурсивную функцию
    hi = len(A) - 1
    Rezy = []
    return binSearchRec(A, elem, 0, hi, Rezy)

def binSearchRec(A: list, elem: int, lo: int, hi: int, Rezy: list):
    # если подмассив пустой, то делать нечего
    if lo > hi:
        return Rezy

    # определяем средний элемент
    mid = (lo + hi) // 2
    Rezy.append(A[mid])

    # выполняем сравнение и рекурсивный вызов на одной из половин
    if A[mid] == elem: return Rezy
    elif A[mid] > elem:
        return binSearchRec(A, elem, lo, mid-1, Rezy)
    else:
        return binSearchRec(A, elem, mid+1, hi, Rezy)
    
if __name__ == "__main__":
    elem = int(input())
    arr = list(map(int, input().split()))
    print(*binSearch(arr, elem))