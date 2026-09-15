class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        i=0
        ans=''
        while i < len(s):
            if s[i].isdigit():
                num = ''
                while i<len(s) and s[i].isdigit():
                    num+=s[i]
                    i+=1
                num = int(num)
                stack.append(num)   
            elif s[i]=='[':
                stack.append(ans)
                ans=''
                i+=1
            elif s[i]==']':
                prev=stack.pop()
                num=stack.pop()
                ans=prev+ans*num
                i+=1
            else:
                ans+=s[i]
                i+=1
        return ans