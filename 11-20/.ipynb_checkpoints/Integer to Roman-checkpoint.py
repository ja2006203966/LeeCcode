class Solution:
    def intToRoman(self, num: int) -> str:
        # L = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        L = ["I", "V", "X", "L", "C", "D", "M"]
        l = [1,5,10,50,100,500,1000]
        x = []
        for i in range(7):
            x.append(num//(l[6-i]))
            num = num%l[6-i]
        s = ""
        x = [x[6-i] for i in range(7) ]
        x = x+[0]
        jp=0
        for i in range(7):
            if jp:
                jp=0
                continue
            if x[i]<=3:
                sp =""
                for j in range(x[i]):
                    sp =  L[i]+sp
            else:
                if x[i]==4 and x[i+1]==1:
                    jp=1
                    sp = L[i]+L[i+2]
                else:
                    sp =L[i+1]
                    for j in range(x[i]-3):
                        sp = L[i]+sp
            s = sp +s
        return s

                
        