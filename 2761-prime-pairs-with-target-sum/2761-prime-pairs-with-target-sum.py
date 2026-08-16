class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n<=2:
            return []
        is_prime=[True]*n
        p=2
        while p*p<=n:
            if is_prime[p]:
                for mul in range(p*p,n,p):
                    is_prime[mul]=False
            p+=1
        ans=[]
        for i in range(2,(n//2)+1):
            if is_prime[i]==True and is_prime[n-i]==True:
                ans.append([i,n-i])
        return ans