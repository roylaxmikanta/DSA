class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer=[]
        for i in range(left,right+1):
            num=i
            no=i
            is_true=True
            while no>0:
                ld=no%10
                if ld==0 or num%ld!=0:
                    is_true=False
                    break
                no=no//10
            if is_true==True:
                answer.append(num)
        return answer