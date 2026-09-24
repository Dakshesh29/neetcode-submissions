class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []
        # for l in range(len(nums)-k+1):
        #     r = l+k-1
        #     max_val = nums[l]

        #     for i in range(l,r+1):
        #         max_val = max(max_val,nums[i])
        #     res.append(max_val)
        # return res

        output = []
        q = deque()  
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output