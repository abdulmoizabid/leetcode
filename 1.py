class Solution(object):
    def containsDuplicate(self, nums):
        n = len(nums)
        highest = max(nums)
        print(highest)
        util_list = [0] * (highest+1)
        for i in range (0, n):
            x = nums[i]
            if(util_list[x] >= 1):
                return True
            else:
                util_list[x] = 1
            
        return False
        
if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]
    a = Solution()
    print(a.containsDuplicate(nums))