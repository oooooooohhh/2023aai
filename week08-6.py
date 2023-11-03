class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        N = len(arr)
        arr.sort()

        for i in range(1, N):
            if arr[i] - arr[i-1] != arr[1] - arr[0]:
                return False
        return True
        