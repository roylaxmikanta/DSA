class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        if n<=2:
            return []
        is_prime=[True]*n
        p=2
        while p**2<n:
            if is_prime[p]!=False:
                i=2
                while p*i<n:
                    is_prime[p*i]=False
                    i+=1
            p+=1
        ans=[]
        for i in range(2,(n//2)+1):
            if is_prime[i]==True and is_prime[n-i]==True:
                ans.append([i,n-i])
        return ans