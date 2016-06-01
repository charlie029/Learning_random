# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 15:40:11 2016

@author: djl358
"""
# question same tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==None and q==None:
            return True
        elif p==None and q!=None:
            return False
        elif q!=None and p==None:
            return False
        elif p.val != q.val:
            return False
        else:
            print p.val            
        # the return a and b structure runs a first and then b
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
a = TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(3)
a.right = TreeNode(4)
a.right.left = TreeNode(5)

b = TreeNode(1)
b.left = TreeNode(2)
b.left.left = TreeNode(3)
b.right = TreeNode(4)
b.right.left = TreeNode(5)

temp = Solution()
temp.isSameTree(a, b)


# question valid anagram
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = list(s)
        t_list = list(t)
        if len(s_list) == len(t_list):
            s_ls = sorted(s_list)
            t_ls = sorted(t_list)
            if s_ls == t_ls:
                return True
            else:
                return False
        else:
            return False

s = 'hello'
t = 'hello'
temp = Solution()
temp.isAnagram(s, t)

# 171. Excel Sheet Column Number
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        l = len(s_list)
        tsum = 0
        i = 0
        for item in s_list:
            tsum += (ord(item)-64)*26**(l-1-i)
            i += 1
        return tsum
s = 'ABCDEFD'
temp = Solution()
temp.titleToNumber(s)

# 217. Contains Duplicate
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        else:           
            nums_s = list(set(nums))
            if len(nums)==len(nums_s):
                return True
            else:
                return False
        


