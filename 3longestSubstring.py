# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 14:38:19 2018

@author: liuyuming
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        N = len(s)
        maxLen = 1
        if(N==0 or N==1): return N
        p1, p2 = s[0], s[1]
        i, j = 0, 1
        substr = []
        substr.append(p1)
        while(j<N):
            p2 = s[j]
            if(p2 in substr):
                if(j-i>maxLen):
                    maxLen = j-i
                i = i+substr.index(p2)+1
                p1 = s[i]
                substr = list(s[i:(j+1)])
            else:
                substr.append(p2)
            j = j+1   
                                
        if(maxLen<j-i):
            maxLen = j-i

        return maxLen
        
        
        
string1 = "abcabcabc" # 3 abc
string2 = "bbbb" # 1 b
string3 = "pwwkew" # 3 kew

a = Solution()
n1 = a.lengthOfLongestSubstring(string1)
n2 = a.lengthOfLongestSubstring(string2)
n3 = a.lengthOfLongestSubstring(string3)
print("{}{}{}".format(n1,n2,n3))

# =============================================================================
# s = string2
# N = len(s)
# maxLen = 1
# #if(N==1): return 1
# p1, p2 = s[0], s[1]
# i, j = 0, 1
# substr = []
# substr.append(p1)
# while(j<N):
#     p2 = s[j]
#     if(p2 in substr):
#         if(j-i>maxLen):
#             maxLen = j-i
#         i = i+substr.index(p2)+1
#         p1 = s[i]
#         substr = s[i:(j+1)]
#     else:
#         substr.append(p2)
#     j = j+1   
#         
#         
# if(maxLen<j-i):
#     maxLen = j-i
# 
# =============================================================================
