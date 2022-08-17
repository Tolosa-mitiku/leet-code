class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = set()
        for word in words:
            transformation = ""
            for letter in word:
                transformation += morsecode[ord(letter)-97]
            transformations.add(transformation)
        return len(transformations)