class Solution:
    def compress(self, chars: List[str]) -> int:
        streak = 1
        last_char = chars[0]
        left = 0
        
        def fillCompressedString(last_char, streak):
            nonlocal left
            chars[left] = last_char
            left += 1

            if streak > 1:
                for ch in str(streak):
                    chars[left] = ch
                    left += 1

        for index, ch in enumerate(chars):
            if index == 0:
                continue
            
            if ch != last_char:
                fillCompressedString(last_char, streak)
                last_char = ch
                streak = 1
            else:
                streak += 1
        
        fillCompressedString(last_char, streak)
        return left