class Solution:
    def compress(self, chars: list[str]) -> int:
        hash_map={}
        ans=''
        count=1
        for i in range(1,len(chars)):
            if chars[i]!=chars[i-1]:
                ans+=(chars[i-1])
                if count!=1:
                    ans+=str(count)
                count=1
            else:
                count+=1
        ans+=(chars[-1])
        if count!=1:
            ans+=(str(count))    
        chars[:]=list(ans)
        return len(chars)