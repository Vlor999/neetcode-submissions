class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for lettre in word:
            if lettre not in node.children:
                node.children[lettre] = TrieNode()
            node = node.children[lettre]
        node.isEnd = True

    def searchIntoTrieNode(self, TrieNodeElem: TrieNode, word: str) -> bool:
        node = TrieNodeElem
        currentPos = 0
        for lettre in word:
            if lettre not in node.children:
                if lettre == ".":
                    for child in node.children:
                        isGood = self.searchIntoTrieNode(node.children[child], word[currentPos + 1:])
                        if isGood:
                            return True
                    return False
                else :
                    return False
            node = node.children[lettre]
            currentPos += 1
        return node.isEnd

    def search(self, word: str) -> bool:
        return self.searchIntoTrieNode(self.root, word)