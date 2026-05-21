class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        def findPivot():
            left, right = 1, mountainArr.length()-2

            while left <= right:
                middle = (left+right) // 2
                left_val, middle_val, right_val = mountainArr.get(middle-1), mountainArr.get(middle), mountainArr.get(middle+1)

                if left_val < middle_val > right_val:
                    return middle
                
                if left_val < middle_val < right_val:
                    left = middle + 1
                else:
                    right = middle - 1
        
        pivot = findPivot()
        left, right = 0, pivot
        while left <= right:
            middle = (left+right) // 2
            middle_val = mountainArr.get(middle)
            
            if middle_val < target:
                left = middle + 1
            elif middle_val > target:
                right = middle - 1
            else:
                return middle
        
        left, right = pivot+1, mountainArr.length()-1
        while left <= right:
            middle = (left+right) // 2
            middle_val = mountainArr.get(middle)

            if middle_val < target:
                right = middle - 1
            elif middle_val > target:
                left = middle + 1
            else:
                return middle
        
        return -1