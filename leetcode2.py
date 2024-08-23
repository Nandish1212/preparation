#kth smallest absolute value:
def asb_value(nums,k):
    def count_pairs(mid):
        cnt, left = 0, 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > mid:
                left += 1
                cnt += right - left
            return cnt
        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            if count_pairs(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
nums=[1,3,1]
k=1
print(asb_value(nums,k))