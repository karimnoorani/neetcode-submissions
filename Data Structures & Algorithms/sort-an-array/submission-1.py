class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(left, right):
            if left == right:
                return [nums[left]]
            
            middle = (left+right) // 2
            left_portion = mergeSort(left, middle)
            right_portion = mergeSort(middle+1, right)

            left_ptr = 0
            right_ptr = 0
            for index in range(left, right+1):
                if left_ptr < len(left_portion) and (right_ptr == len(right_portion) or left_portion[left_ptr] < right_portion[right_ptr]):
                    nums[index] = left_portion[left_ptr]
                    left_ptr += 1
                else:
                    nums[index] = right_portion[right_ptr]
                    right_ptr += 1
            
            return nums[left:right+1]
        
        return mergeSort(0, len(nums)-1)