class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Iterative Approach: Python String Methods with Two Pointers
        """
        left, right = 0, len(s) - 1

        while left < right:
             
            # Step 1: Skip non-alphanumeric characters.
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Step 2: Compare characters to check if palindrome. 
            if s[left].lower() != s[right].lower():
                return False
            
            # Step 3: Update pointers.
            left += 1
            right -= 1
        
        return True

        # O(n) time.
        # O(1) auxiliary space.
        # O(n) total space.


    def isPalindrome2(self, s: str) -> bool:
        """
        Iterative Approach: Custom String Methods with Two Pointers
        """
        def is_alphanum(char):
            return (ord('0') <= ord(char) <= ord('9') or
                    ord('a') <= ord(char) <= ord('z') or
                    ord('A') <= ord(char) <= ord('Z'))
        
        def to_lower(char):
            if ord('A') <= ord(char) <= ord('Z'):
                return chr(ord(char) + 32)
            return char

        left, right = 0, len(s) - 1

        while left < right:
             
            # Step 1: Skip non-alphanumeric characters.
            while left < right and not is_alphanum(s[left]):
                left += 1
            while left < right and not is_alphanum(s[right]):
                right -= 1

            # Step 2: Compare characters to check if palindrome. 
            if to_lower(s[left]) != to_lower(s[right]):
                return False
            
            # Step 3: Update pointers.
            left += 1
            right -= 1
        
        return True

        # O(n) time.
        # O(1) auxiliary space.
        # O(n) total space.


    def isPalindrome3(self, s: str) -> bool:  
        """
        Iterative Approach: Pythonic Way
        """
        new_s = "".join(char.lower() for char in s if char.isalnum())
        return new_s == new_s[::-1]