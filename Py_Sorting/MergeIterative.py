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

def mergeSortNonRec(A):
    # запоминаем длину массива
    n = len(A)

    # инициализируем переменную, в которой будем хранить длину сливаемых массивов
    width = 1

    # запускаем внешний цикл, который будет перебирать удваивающиеся значения width
    while width < n:
        i = 0
        # запускаем цикл, который будет сливать половины подмассивов размером 2*width
        while i < n:
            min1 = min(i+width-1, n-1)
            min2 = min(i+2*width-1, n-1)
            merge(A, i, min1, min2)
            # не забываем увеличивать i на нужное значение
            i = i + 2 * width
        # не забываем увеличивать width на нужное значение
        width *= 2

        # выводим массив в нужном формате
        print(*A)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    
    mergeSortNonRec(arr)