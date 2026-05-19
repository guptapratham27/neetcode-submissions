class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        i=0
        num=sorted(nums)
        for i in range(len(num)-1):
            j=i+1
            if(num[i]==num[j]):
                return True;
            else:
                i=i+1
                j=j+1
        
        return False;
            
        