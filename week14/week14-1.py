class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notAns = set()


        for a,b in paths:
            notAns.add(a)#出發點,不是答案


        for a,b in paths: #第2輪
            if b not in notAns:#b不再出發裡,就是答案
                return b #b 不是「不是答案」