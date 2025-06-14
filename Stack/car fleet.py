place holder
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        '''
            using python deque
                - similar methods
                - popleft()
                - appendleft()
                - just allowing to append left and right 
            using match 
                match case: 
                else could be written as case _:
            
            Difference between isnumeric and isdigit
                - isnnumeric accounts for isdigit
                - accounts for roman numerals as well

            import math.ciel
            take one argument
            match.ciel

            Read direction carefully 
                - truncates towards zero
                    
        '''

        #stack (python deque) to put the polish notation 
        #once we enconunter a number we will pop 2 times
        stack  = deque()

        #Use a for loop to keep iterating until all tokens have been processed
        for token in tokens: 
            
            
            match token: 
                
                #Addition
                case '+':
                    numTwo = stack.pop()
                    numOne = stack.pop()
                    stack.append(numOne + numTwo)
                    print()

                #Subtraction 
                case '-':
                    numTwo = stack.pop()
                    numOne = stack.pop()
                    stack.append(numOne - numTwo)
                    
                #Division
                case '/':
                    numTwo = stack.pop()
                    numOne = stack.pop()
                    
                    #Truncates Towards Zero
                    #Get Ceiling if the result is negative
                    if (numOne // numTwo) < 0:
                        stack.append(math.ceil(numOne/numTwo))
                    #Else get the floor value (number is positive)
                    else:
                        stack.append(numOne // numTwo)
                
                #Multiplication
                case '*': 
                    numTwo = stack.pop()
                    numOne = stack.pop()
                    stack.append(numOne * numTwo)
                
                #Will be a number / Guarantee 
                case _:
                    stack.append(int(token))
        
        return stack[-1]
