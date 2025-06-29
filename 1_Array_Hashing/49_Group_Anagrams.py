class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        Important Concept
        - Keys in Python Dictionaries have to be immutable
        - Tuples are data type that are immutable and ordered 
        - ord (python function) returns the unicode integer value
        - defaultdict automatically initializes a key with a default value of the specified type when the key does not exist.
        ''' 

        #Create a dictionary to group anagrams
        #Wants keys to be the frequency of letters 
        #This tells if it is an anagram
        #Anagram = freq. of letters -> cat = tac or catt == ttac 
        groupAnagrams = defaultdict(list)

        #iterate through each of the words within the give list of strings
        for word in strs:

            #Temporary Array to be used as a key 
            #26 letters in the alphabet -> list of size 26 
            #Keep Frequencies of Characters in each Word 
            temp = [0] * 26

            #Go through each letter in the word and count the frequencies 
            for letter in word: 
                
                #Use ord function to grab index value of letter
                #example z - a (unicode values) = 26
                index = ord(letter) - ord('a')
                temp[index] +=1
            
            #Convert temp to a tuple to make it immutable and create a the key
            key = tuple(temp)

            groupAnagrams[key].append(word)
        
        answerGA  = list(groupAnagrams.values())
        return answerGA

    
  
