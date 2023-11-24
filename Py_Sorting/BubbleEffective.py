def BubbleSort(nums: list) -> list:
    temp = nums
    for i in range(len(temp) - 1):
        ok = True
        for j in range(len(temp) - 1 - i):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                ok = False
        yield temp
        if ok == True:
            return temp

input = list(map(int, input().split()))

for i in BubbleSort(input):
    print(*i)
