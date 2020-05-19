class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self._int(num1) * self._int(num2))
        
    def _int(self, num):
        power = len(num) - 1
        _sum = 0
        
        # multiply by 10: 123 = 1*10*10+2*10+3
        for i in num:
            _sum += (ord(i) - ord('0')) * (10**power)
            power -= 1
        
        
        return _sum
