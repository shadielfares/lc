class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        #This should split it by whitespace, or new line characters
        words_in_sentence = sentence.split()
        #first for loop iterates all words in sentence
        for word in range(len(words_in_sentence)):
            #-1 im python == len(w -1) which gets the last character
            if words_in_sentence[word][0] != words_in_sentence[word-1][-1]:
                return False
        return True