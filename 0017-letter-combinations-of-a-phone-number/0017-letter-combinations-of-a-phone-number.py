class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        answer=[]
        def solve(index,subset):
            if len(subset)>=len(digits):
                answer.append(''.join(subset))
                return
            for ch in char_map[digits[index]]:
                subset.append(ch)
                solve(index+1,subset)
                subset.pop()
        solve(0,[])
        return answer