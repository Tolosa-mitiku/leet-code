class Solution:
    
    def f(self,target,index,nums,dp):
        
        if target==0:
		    dp[index][target]=True
            return dp[index][target]
        if index==0: 
			dp[index][target]=nums[index]==target
			return dp[index][target]
        if dp[index][target]!=-1:
            return dp[index][target]==target
        nottaken=self.f(target,index-1,nums,dp)
        taken=False
        if nums[index]<=target:
            taken=self.f(target-nums[index],index-1,nums,dp)
        dp[index][target]= taken or nottaken
        return dp[index][target]
        
        
    def minimumDifference(self, nums: List[int]) -> int:
        n=len(nums)
        m=min(nums)
        totalsum=sum(nums)
        dp=[[-1 for _ in range(totalsum+1)] for _ in range(n)]
        for target in range(totalsum):
            dummy=self.f(target,n-1,nums,dp)
        
        minimum=10e9
        for target in range(totalsum):
            if dp[n-1][target]==True:
                minimum=min(minimum,abs(target-(totalsum-target)))
        return minimum
                