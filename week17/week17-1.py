class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N=len(nums)# 問題的長度
        ans = 1
        table = [0]*N #放小達隘的表格
        table[0] = 1 #最簡單的問題答案就是我自己1個字
        for i in range(1,N): #慢慢探索更多的答案 table[i]
            table[i] = 1 #最簡單的答案
            for k in range(i): # 我要去查 table[0]...table[i-1]
                if nums[i]>nums[k] and table[k]+1>table[i]: 
                    #我比你大可以吃你 而且你的答案+我一個會比我原本記下的更好
                    
                    table[i] = table[k]+1 
                    #經過上面逐項檢查 確認table[i]就是問題nums[i]的對應答案

            if table[i] > ans: ans = table[i]# 更新最後最大的答案
        return ans