def InsertSort(nums: list) -> list:
    temp = nums
    for i in range(1, len(temp)):
        elem = temp[i]
        index = i
        while index > 0 and elem < temp[index - 1]:
            temp[index] = temp[index - 1]
            index -= 1
        temp[index] = elem
        yield temp

input = list(map(int, input().split()))

for i in InsertSort(input):
    print(*i)
