def quickSort3Way(A: list, left = 0, right = None, verbose = False) -> list:
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right:
        return 

    # инициализируем всевозможные указатели
    lt = left
    gt = right
    v = A[left]
    i = left

    # производим трехпутевое разбиение за один проход в соответствии с алгоритмом
    while i <= gt:
        if A[i] < v:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        
        elif A[i] > v:
            A[gt], A[i] = A[i], A[gt]
            gt -= 1
            
        else:
            i += 1

    # печатаем массив в нужном формате
    print(*A)

    # рекурсивно сортируем обе части (кроме той, что равна опорному элементу!)
    quickSort3Way(A, left, lt-1)
    quickSort3Way(A, gt+1, right)

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    verbose = False
    
    try:
        if input() == "verbose":
            verbose = True
    except:
        pass
    finally:
        quickSort3Way(arr, verbose)