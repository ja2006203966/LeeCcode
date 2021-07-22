class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        L = {"2":"abc","3": "def", "4":"ghi","5": "jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz" }
        digits = digits[::-1]
        C = "@".join(L[digits[0]])
        if len(digits)>1:
            for d in digits[1:]:
                c = C.split("@")
                C = ""
                for i in range(len(c)):
                    c[i] = (c[i]+"@").join(L[d])+c[i]+"@"
                for i in c:
                    C += i
                C = C[:-1]
        # C = [C[i:i+len(digits)] for i in range(len(C)-len(digits) )]
        return C.split("@")