class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N =len(strs)
        s= strs[0]
        m=len(s)
        ans = ""
        b=0
        for n in range(m+1):
            for k in range(N):
                if s[0:n]!=strs[k][0:n]:
                    b=1
                    break
            if b==1:
                break
            else:
                ans = s[0:n]
        return ans