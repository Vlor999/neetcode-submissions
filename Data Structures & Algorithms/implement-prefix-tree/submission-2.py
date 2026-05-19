#! /usr/bin/env python3

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def __str__(self, level=0):
        result = []
        indent = "  " * level
        for key, child in self.children.items():
            result.append(f"{indent}{key} -> {child.__str__(level + 1)}")
        if self.isEnd:
            result.append(f"{indent}(end)")
        return "\n".join(result)

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def __str__(self):
        return self.root.__str__()

    def insert(self, word: str) -> None:
        node = self.root
        for lettre in word:
            if lettre not in node.children:
                node.children[lettre] = TrieNode()
            node = node.children[lettre]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for lettre in word:
            if lettre not in node.children:
                return False
            node = node.children[lettre]
        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for lettre in prefix:
            if lettre not in node.children:
                return False
            node = node.children[lettre]
        return True
