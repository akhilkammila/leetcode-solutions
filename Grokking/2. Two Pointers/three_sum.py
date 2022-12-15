class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        answ=set()
        nums.sort()
        
        for i in range(len(nums)): #0 through 5
            first_num=nums[i]
            
            left=i+1
            right=len(nums)-1
            
            #use 2 pointers to check for all possibilities
            while left<right:
                total = nums[left]+nums[right]+first_num
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    answ.add(tuple([first_num, nums[left], nums[right]]))
                    left+=1
                    right-=1
        return answ