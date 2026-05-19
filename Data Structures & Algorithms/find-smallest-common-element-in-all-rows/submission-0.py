class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        lower_bound, upper_bound = float('inf'), float('-inf')

        for row in range(ROWS):
            lower_bound = min(lower_bound, mat[row][0])
            upper_bound = max(upper_bound, mat[row][COLS-1])
        
        def binarySearch(row, val):
            left, right = 0, COLS-1

            while left <= right:
                middle = (left + right) // 2

                if row[middle] < val:
                    left = middle + 1
                elif row[middle] > val:
                    right = middle - 1
                else:
                    return True
            
            return False

        def isPresentAllRows(val):
            for row in mat:
                if not binarySearch(row, val):
                    return False
            return True

        for num in range(lower_bound, upper_bound+1):
            if isPresentAllRows(num):
                return num
        
        return -1
            