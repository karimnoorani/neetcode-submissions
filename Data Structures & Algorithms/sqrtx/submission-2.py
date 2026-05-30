class Solution:
    def mySqrt(self, x: int) -> int:
        lower_bound, upper_bound = 0, x
        result = x
        while lower_bound <= upper_bound:
            middle = (lower_bound + upper_bound) // 2
            squared_num = middle * middle

            if squared_num < x:
                result = middle
                lower_bound = middle + 1
            elif squared_num > x:
                upper_bound = middle - 1
            else:
                return middle
        
        return result