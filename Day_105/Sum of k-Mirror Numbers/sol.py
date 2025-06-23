class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(num, k):
            res = []
            while num > 0:
                res.append(str(num % k))
                num //= k
            return ''.join(reversed(res))

        def generate_palindromes():
            length = 1
            while True:
                for half in range(10 ** (length - 1), 10 ** length):
                    s = str(half)
                    yield int(s + s[-2::-1])  
                for half in range(10 ** (length - 1), 10 ** length):
                    s = str(half)
                    yield int(s + s[::-1])    
                length += 1


        gen = generate_palindromes()
        count = 0
        total = 0

        while count < n:
            
            num = next(gen)
            if is_palindrome(to_base_k(num, k)):
                print(num)
                total += num
                count += 1

        return total
