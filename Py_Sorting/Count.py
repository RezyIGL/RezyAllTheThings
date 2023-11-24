def countSort(nums: list) -> str:
    index = 0
    dlinaNumsa = len(nums)
    Ck = [0] * dlinaNumsa
    k = max(nums) + 1
    
    for i in range(dlinaNumsa):
        Ck[nums[i]] += 1
        
    for j in range(k):
        nums[index:index + Ck[j]] = [j] * Ck[j]
        index += Ck[j]
        
    return nums

print(*countSort(list(map(int, input().split()))))