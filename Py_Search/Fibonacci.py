def Fiba(n: int) -> int:
    f0 = 0
    f1 = 1
    f = 0
    for i in range(n):
        f = f0 + f1
        f0, f1 = f1, f0+f1
    return f

def fibSearch(A: list, elem: int) -> list:
    Rezy = []
    hi = len(A)
    # если искомый элемент за границами диапазона,то делать нечего
    if elem < A[0] or elem > A[hi-1]:
        return [None]

    # вычисляем нужное число Фибоначчи
    for i in range(hi+2):
        fk = Fiba(i)
        if fk >= hi:
            k = i
            break
 
    # вызываем рекурсивную функцию
    return fibSearchRec(A, elem, 0, Fiba(k-1), fk, hi, Rezy)

def fibSearchRec(A: list, elem: int, lo: int, fKm1: int, fK: int, n: int, Rezy: list) -> list:
    # если подмассив пустой ИЛИ из одного элемента, который не равен elem, то делать нечего
    if fK == 0 or (fK == 1 and A[lo] != elem):
        Rezy.append(A[lo])
        return Rezy

    # если подмассив из одного элемента, который равен elem, то возвращаем ответ и завершаемся
    if fK == 1 and A[lo] == elem:
        Rezy.append(A[lo])
        return Rezy

    # вычисляем (k-2)-е число Фибоначчи
    fKm2 = fK - fKm1

    # вычисляем mid - правый элемент первого подмассива (смотрим, чтобы он не выпал за границы)
    mid = min(lo + fKm2 - 1, n - 1)
    Rezy.append(A[mid])
    
    # выполняем сравнение и рекурсивный вызов на одной из частей
    if A[mid] == elem:
        return Rezy
    if A[mid] > elem:
        return fibSearchRec(A, elem, lo, fKm1-fKm2, fKm2, n, Rezy)
    else:
        return fibSearchRec(A, elem, lo+fKm2, fKm2, fKm1, n, Rezy)
    
if __name__ == "__main__":
    elem = int(input())
    arrA = list(map(int, input().split()))
    print(*fibSearch(arrA, elem))