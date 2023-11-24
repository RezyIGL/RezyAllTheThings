def verboseBuilder(array: list, left: int, mid: int, right: int) -> str:
    result = array.copy()
    temp = [None] * 2
    if left > mid - 1:
        temp[0] = mid

    if right < mid + 1:
        temp[1] = mid + 1

    if temp[0] is None:
        if left == mid - 1:
            result[left] = f'[{array[left]}]'
        else:
            result[left] = f'[{array[left]}'
            result[mid - 1] = f'{array[mid - 1]}]'

    if temp[1] is None:
        if right == mid + 1:
            result[right] = f'[{array[right]}]'
        else:
            result[mid + 1] = f'[{array[mid + 1]}'
            result[right] = f'{array[right]}]'

    for i in temp:
        if not i is None:
            result.insert(i, [])
    return result

def partition(A: list, left: int, right: int) -> int:
    i = left + 1
    j = right

    while i <= j:
        while i < right and A[i] < A[left]:
            i += 1 

        while j > left and A[j] > A[left]:
            j -= 1

        if i >= j:
            break
        
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

    A[left], A[j] = A[j], A[left]
    return j

def quickSort(A: list, left = 0, right = None, verbose = False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    lenArr = len(A)
    if right == None:
        right = lenArr - 1

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right:
        return

    # производим разбиение с помощью partition
    p = partition(A, left, right)
    # печатаем массив
    if verbose:
        print(*verboseBuilder(A, left, p, right))
    else:
        print(*A)

    # рекурсивно сортируем обе части
    quickSort(A, left, p - 1, verbose)
    quickSort(A, p + 1, right, verbose)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    verbose = False
    
    try:
        if input() == "verbose":
            verbose = True
    except EOFError:
        pass
    finally:
        quickSort(arr, verbose=verbose)