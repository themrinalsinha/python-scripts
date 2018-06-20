def consecutive(nums):
    nums    = list(set(nums))
    ranges  = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
    iranges = iter(nums[0:1] + ranges + nums[-1:])
    return ', '.join([str(n) + '-' + str(next(iranges)) for n in iranges])

num = [100, 101, 102, 103, 104, 109, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
res = consecutive(num)
print(res)
