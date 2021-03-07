nums = input().split()
lenght = len(nums)
#print(lenght)
cnt = 0
for i in range(lenght - 1):         
    for j in range(i+1, lenght):
            #print(nums[i],nums[j])
            if nums[i] == nums[j]:
                cnt += 1
print(cnt)