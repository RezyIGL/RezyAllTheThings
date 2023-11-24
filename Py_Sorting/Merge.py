def verboseBuilder(A: list, left: int, mid: int, right: int, lenArr: int) -> str:
    returnList = [None] * lenArr
    for i in range(lenArr):
        if i == left == mid or i == right == mid + 1:
            returnList[i] = [A[i]]
        elif i == left or i == mid + 1:
            returnList[i] = f"[{A[i]}"
        elif i == right or i == mid:
            returnList[i] = f"{A[i]}]"
        else:
            returnList[i] = f"{A[i]}"
    return returnList

def merge(A: list, left: int, mid: int, right: int) -> list:
    AUX = []

    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            AUX.append(A[i])
            i += 1
        
        else:
            AUX.append(A[j])
            j += 1

    if i >= mid:
        AUX.extend(A[j:right + 1])

    if j >= right:
        AUX.extend(A[i:mid + 1])

    A[left:right + 1] = AUX

def mergeSort(A: list, left = 0, right = None, verbose = False) -> list:
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    lenArr = len(A)
    if right == None:
        right = lenArr - 1

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right:
        return

    # определяем середину
    mid = (left + right) // 2

    # рекурсивно сортируем обе половины
    mergeSort(A, left, mid, verbose)
    mergeSort(A, mid + 1, right, verbose)

    # печатаем массив и производим слияние с помощью функции merge
    if verbose:
        print(*verboseBuilder(A, left, mid, right, lenArr))
    else:
        print(*A) 
    merge(A, left, mid, right)

# читаем список A (и возможно слово 'verbose' на второй строке)
if __name__ == "__main__":
    arr = list(map(int, input().split()))

    try:
        if input() == "verbose":
            verbose = True
    except EOFError:
        verbose = False
    finally:
        mergeSort(arr, 0, None, verbose)
        print(*arr)