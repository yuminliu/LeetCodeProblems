# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:10:57 2018

@author: liuyuming
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a = ListNode(5)
b = ListNode(3)
c = ListNode(7)
d = ListNode(6)
a.next = b
c.next = d

l1 = a
l2 = c

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        val = (l1.val+l2.val+flag)
        digit = val%10
        flag = int((val/10)>=1)
        print("digit and flag is {}{}".format(digit,flag))
        addSum = ListNode(digit)
        result = addSum
        print(addSum.val)
        a, b = l1.next, l2.next
        while(a!=None and b!=None):
            val = (a.val+b.val+flag)
            digit = val%10
            flag = int((val/10)>=1)
            print("ab: digit and flag is {}{}".format(digit,flag))
            addSum.next = ListNode(digit)
            a, b, addSum = a.next, b.next, addSum.next
            print(addSum.val)
        #addSum = addSum.next
        while(a!=None):
            val = a.val+flag
            digit = val%10
            flag = int((val/10)>=1)
            print("a: digit and flag is {}{}".format(digit,flag))
            addSum.next = ListNode(digit)
            a, addSum = a.next, addSum.next
        while(b!=None):
            val = b.val+flag
            digit = val%10
            flag = int((val/10)>=1)
            print("b:digit and flag is {}{}".format(digit,flag))
            addSum.next = ListNode(digit)
            b, addSum = b.next, addSum.next
        if(flag):
            addSum.next = ListNode(flag)
        
        return result
        
clsaaa = Solution()
addSum = clsaaa.addTwoNumbers(l1,l2)        
ll1, ll2, aa = l1, l2, addSum
while(ll1!=None):
    print(ll1.val)
    ll1 = ll1.next
while(ll2!=None):
    print(ll2.val)
    ll2 = ll2.next        
while(aa!=None):
    print(aa.val)
    aa = aa.next          
        
