class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==0:
            return 0
        hashset=set()
        count=0
        for i in s:
            if i not in hashset:
                hashset.add(i)
            else:
                hashset.remove(i)
                count+=2
        if(len(hashset)==0):
            return count
        else:
            return count+1
            
#time Complexity is O(n) as whole string is traversed
#space complecity is O(1)
