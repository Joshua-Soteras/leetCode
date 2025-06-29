class Solution:
    def isValid(self, s: str) -> bool:

        '''
        Important Skills
        - Stack in Python uses list 
        - Peek ->  stack[-1]
        - 
        '''

        if len(s) % 2 != 0:
            return False

        #Dictionary of Paratheses
        pairs = {')':'(' , '}':'{' , ']':'['}

        #Stack that will be used to store opening brackets
        #Will pop when encountering matching closing bracket 
        stack = []

        #Iterate through the string
        for character in s: 

            #If nothing is within the stack means that the string begins with an closing bracket
            # Return false because valid parentheses cannot begin with a closing bracket
            if (not stack) and (character in pairs):
                return False 
            
            #If the character is a closing parentheses  
            #And if the top of the stack is the matching opening parentheses, we found a pair 
            #Then we pop
            elif character in pairs and stack[-1] == pairs[character]:

                stack.pop()
            
            #Else: the character is an open bracket in which we push to the stack
            else:
                stack.append(character)

            
        #If the stack is empty, then all paretheses have matching pairs (valid)
        if not stack:
            return True
        #Else there missing matching closing parentheses 
        else:
            return False
