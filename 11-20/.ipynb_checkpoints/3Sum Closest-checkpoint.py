class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N = len(nums)
        nums = sorted(nums)
        L = 1e5
        ans=0
        for i in range(N-2):
            j, k = i+1, N-1
            while(j<k):
                sm = nums[i]+nums[j]+nums[k]
                if abs(sm-target)<L:
                    L = abs(sm-target)
                    ans=sm
                    if sm-target>0:
                        k-=1
                    elif sm-target<0:
                        j+=1
                    elif sm== target:
                        return sm
                elif sm-target>0:
                    k-=1
                elif sm-target<0:
                    j+=1
        return ans
    
                
        