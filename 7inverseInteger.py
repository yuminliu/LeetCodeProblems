# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:09:54 2018

@author: liuyuming
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #x = -120
        flag = 0
        if(x<0):
            x = -x
            flag = 1
        
        result = 0
        while(x!=0):
            result = result*10 + (x%10)
            x = int(x/10)
        
        if(flag):
            result = -result
        if((result<-2**31) or (result>2**31-1)):
            result = 0
        return result
    
#x = 1534236469
#a = Solution()
#result = a.reverse(x)