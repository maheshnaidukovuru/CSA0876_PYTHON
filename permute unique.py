def permuteUnique(nums):
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        seen = set()
        for i in range(start, len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

    result = []
    nums.sort()
    backtrack(0)
    return result
nums = [1, 1, 2]
print("Output for Test Case 1:", permuteUnique(nums))