class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def products(x):
            product=1
            while x>0:
                ld=x%10
                product*=ld
                x//=10
            return product
        while products(n)%t!=0:
            n+=1
        return n