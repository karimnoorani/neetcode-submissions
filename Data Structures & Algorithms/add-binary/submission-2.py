class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        res = [0 for _ in range(max(len(a), len(b))+1)]

        a, b = a[::-1], b[::-1]

        def add(i, carry):
            if i >= len(a) and i >= len(b) and not carry:
                return
            
            intB = int(b[i]) if i < len(b) else 0
            intA = int(a[i]) if i < len(a) else 0
            res[i] = (intB+intA+carry)%2
            add(i+1, (intB+intA+carry)//2)
        
        add(0, 0)
        while res and res[-1] == 0:
            res.pop()
        res = list(map(str, res))
        return "".join(res[::-1])