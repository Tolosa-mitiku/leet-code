class Node:
    def __init__(self):
        self.children = {}
        self.count = 1
class TrieNode:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter in curr.children:
                curr.children[letter].count += 1
            else:
                curr.children[letter] = Node()
            curr = curr.children[letter]
    def search(self, word):
        count = 0
        curr = self.root
        for letter in word:
            if letter in curr.children:
                count += curr.children[letter].count
                curr = curr.children[letter]
        return count
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = TrieNode()
        for word in words:
            trie.insert(word)
        ans = []
        for word in words:
            ans.append(trie.search(word))
        return ans