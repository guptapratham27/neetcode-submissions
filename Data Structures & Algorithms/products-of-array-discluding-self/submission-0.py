class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        newl=[]
        for i in nums:
            newl.append(i)
        result=[]

        for i in nums:

            newl.remove(i)
            product=1
            for j in newl:
                product=j*product
            
            result.append(product)
            newl=nums.copy()
        
        return result

        