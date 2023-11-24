def hSort(nums: list) -> list:
    gaps, temp = nums[0], nums[1]

    for gap in gaps:
        for i in range(gap, len(temp)):
            elem = temp[i]
            index = i
            while index >= gap and elem < temp[index - gap]:
                temp[index] = temp[index - gap]
                index -= gap
            temp[index] = elem
        yield temp

input = list(map(int, input().split())), list(map(int, input().split()))

for i in hSort(input):
    print(*i)
