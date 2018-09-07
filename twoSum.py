class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 or isinstance(nums,list) ==False:
            return None

        """
          loop vector find exactly elements 
          
        """
        L=[]
        lens=len(nums)
        print(lens)
        i=0
        j=i

        while i < lens:
            j=i+1
            while j  < lens:
                if nums[i] + nums[j] ==target:
                    L.append(nums[i])
                    L.append(nums[j])
                    j += 1
                else :
                    j += 1
                    continue

            i+=1

        return L










print("x>>>>>>>>>>")

s=Solution()
L=[1,2,3,4,5]
print(L)
S=s.twoSum(L,5)
print(S)

#container=s.twoSum(L,3)
#print(len(container))
#print(container)

