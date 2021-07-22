class Solution:
    def romanToInt(self, s: str) -> int:
        D = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000,"@":0}
        s =s+"@"
        v=0
        vp =0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                vp+=D[s[i]]
            if D[s[i+1]]>D[s[i]]:
                v = v-vp-D[s[i]]
                vp=0
            if D[s[i+1]]<D[s[i]]:
                v+=D[s[i]]+vp
                vp=0
        return v