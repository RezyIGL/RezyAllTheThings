def stableCountSort(rank: int, nums: list) -> list:
    dlina = len(nums)
    maxRank = len(str(max(nums)))
    cnt = [[] for aboba in range(10)]
    for i in range(dlina):
        cnt[int(str(nums[i]).zfill(maxRank)[-rank - 1])].append(nums[i])
    index = 0
    for j in range(10):
        for x in cnt[j]:
            nums[index] = int(x)
            index += 1
    return nums

def CifralSort(nums: list) -> list:
    maxRank = len(max(nums, key=lambda x: int(len(x))))
    for r in range(maxRank):
        print(*stableCountSort(r, nums))

CifralSort(input().split())