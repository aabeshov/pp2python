nums = [int(i) for i in input().split()]
mini = 1001
for i in range(len(nums)):
    if nums[i] < 0:
        nums[i] = 0
for i in range(len(nums)):
    if nums[i] != 0 and nums[i] < mini:
        mini = nums[i]
print(mini)