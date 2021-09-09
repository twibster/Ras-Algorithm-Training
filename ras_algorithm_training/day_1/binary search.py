def search(nums, target):
    nums.sort()
    low =0
    high =len(nums)-1
    while low<=high:
        mid =(high +low)//2
        if target ==nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid+1
        else:
            high =mid -1
    return -1
        