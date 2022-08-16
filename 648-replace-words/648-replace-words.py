class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
            current = current.children[letter]
        current.isWord = True
    def search_successor(self, word: str) -> bool:
        current = self.root
        ans = []
        for letter in word:
            if current.isWord == True:
                return "".join(ans)
            if letter not in current.children:
                return -1
            ans.append(letter)
            current = current.children[letter]
        return -1
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        firstTrie = Trie()
        for root in dictionary:
            firstTrie.insert(root)
        split_sentence = sentence.split()
        for i in range(len(split_sentence)):
            somte = firstTrie.search_successor(split_sentence[i])
            if somte != -1:
                split_sentence[i] = somte
        return " ".join(split_sentence)