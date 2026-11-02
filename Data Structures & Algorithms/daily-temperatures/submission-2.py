class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = []
        # for i in range(len(temperatures)):
        #     count = 1
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[j]>temperatures[i]:
        #             res.append(count)
        #             break
        #         count +=1
        #     else:
        #         res.append(0)
        # return res 

        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][0]:
                T,I = stack.pop()
                res[I] = (i-I)
            stack.append([temp,i])
        return res

            