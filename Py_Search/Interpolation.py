def interpolSearch(A: list, elem: int) -> list:
    hi = len(A) - 1
    Rezy = []
    # если искомый элемент за границами диапазона,то делать нечего
    if elem > A[hi] or elem < A[0]:
        return [None]
    
    # определим верхнюю границу и вызовем рекурсивную функцию
    return interpolSearchRec(A, elem, 0, hi, Rezy)

def interpolSearchRec(A: list, elem: int, lo: int, hi: int, Rezy: list) -> list:
    # если подмассив пустой ИЛИ elem за границами диапазона, то делать нечего
    if lo > hi or (elem > A[hi] or elem < A[lo]):
        return Rezy
    
    # если левая и правая границы совпадают, то mid по формуле вычислять нельзя! (почему?)
    if A[lo] == A[hi]:
        return Rezy + [A[lo]]
    
    # иначе - вычисляем mid по формуле
    else:
        mid = lo + round((elem - A[lo])*((hi - lo)/(A[hi] - A[lo])))
    Rezy.append(A[mid])
    # выполняем сравнение и рекурсивный вызов на одной из частей
    if A[mid] == elem: 
        return Rezy
    elif A[mid] > elem: 
        return interpolSearchRec(A, elem, lo, mid-1, Rezy)
    else:
        return interpolSearchRec(A, elem, mid+1, hi, Rezy)
    
if __name__ == "__main__":
    elem = int(input())
    arrA = list(map(int, input().split()))
    print(*interpolSearch(arrA, elem))