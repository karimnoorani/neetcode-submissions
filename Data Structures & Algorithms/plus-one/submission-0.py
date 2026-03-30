class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def helper(carry):
            if len(digits) == 0:
                return [] if not carry else [carry]
            
            n = digits.pop()

            return helper((n+carry)//10) + [(n+carry)%10]
        
        return helper(1)
            