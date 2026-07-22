class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans=[0]*num_people
        num=1
        i=0
        while candies!=0:
            if num<=candies:
                ans[i]+=num
                candies-=num
                num+=1
                i+=1
                i=i%num_people
            else:
                ans[i]+=candies
                candies=0
        return ans