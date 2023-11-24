def SelectSort(nums: list) -> list:
    temp = nums
    for i in range(len(temp)-1):
        j = temp.index(min(temp[i:]))
        temp[i], temp[j] = temp[j], temp[i]
        yield temp

input = list(map(int, input().split()))

for i in SelectSort(input):
    print(*i)
