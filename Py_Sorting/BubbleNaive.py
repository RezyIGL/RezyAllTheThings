def NaiveBubbleSort(nums: list) -> list:
    temp = nums
    for i in range(len(temp) - 1):
        for j in range(len(temp) - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
        yield temp

input = list(map(int, input().split()))

for i in NaiveBubbleSort(input):
    print(*i)