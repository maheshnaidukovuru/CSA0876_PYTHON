nums = [1, 1, 2]
permutations = [[]]
for num in nums:
    new_perms = []
    for perm in permutations:
        for i in range(len(perm) + 1):
            new_perms.append(perm[:i] + [num] + perm[i:])
            if i < len(perm) and perm[i] == num:
                break
    permutations = new_perms
print(permutations)