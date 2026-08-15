class Solution(object):
    def isPalindrome(self, s):
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()
           

        left = 0
        right = len(clean) - 1
        while left < right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else: 
                return False    
        return True        

            
    
            
        
     
        