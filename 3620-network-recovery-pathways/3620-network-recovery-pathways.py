from collections import deque
from typing import List
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n=len(online)
        graph=[[] for _ in range(n)]
        indeg=[0]*n
        costs=[]
        for u,v,c in edges:
            graph[u].append((v,c))
            indeg[v]+=1
            costs.append(c)
        q=deque(i for i in range(n) if indeg[i]==0)
        topo=[]
        while q:
            u=q.popleft()
            topo.append(u)
            for v,_ in graph[u]:
                indeg[v]-=1
                if indeg[v]==0:
                    q.append(v)
        def check(limit):
            INF=float('inf')
            dp=[INF]*n
            dp[0]=0
            for u in topo:
                if dp[u]==INF:
                    continue
                if u!=0 and u!=n-1 and not online[u]:
                    continue
                for v,c in graph[u]:
                    if c<limit:
                        continue
                    if v!=n-1 and not online[v]:
                        continue
                    dp[v]=min(dp[v],dp[u]+c)
            return dp[n-1]<=k
        if not costs:
            return -1
        l=min(costs)
        r=max(costs)
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans