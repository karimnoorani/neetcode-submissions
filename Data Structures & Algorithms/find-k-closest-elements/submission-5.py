class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.append(float('inf'))
        for index in range(k-1, len(arr)-1):
            left_diff = abs(x-arr[index-k+1])
            right_diff = abs(x-arr[index+1])
            if left_diff < right_diff or (left_diff == right_diff and arr[index-k+1] < arr[index+1]):
                return arr[index-k+1:index+1]