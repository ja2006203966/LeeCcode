class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums = sorted(nums)
        for i in range(n-2):
            j = i+1
            k = n-1
            if nums[i]+nums[i+1]+nums[i+2]>0:
                break
            while( j<k):
                s = nums[i]+nums[j]+nums[k]
                if s==0 :
                    if not ([nums[i], nums[j], nums[k]] in ans):
                        ans.append([nums[i], nums[j], nums[k]])
                    k-=1
                    j+=1
                elif s>0:
                    k-=1
                else:
                    j+=1
            
        return ans