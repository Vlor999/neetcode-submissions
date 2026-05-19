# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "[]"
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return str(result)
    
    def convListToTree(self, currentList: list[int]) -> TreeNode:
        if currentList == []:
            return None
        root = TreeNode(currentList[0])
        queue = deque([root])
        i = 1
        while i < len(currentList):
            node = queue.popleft()
            if currentList[i] != None:
                node.left = TreeNode(currentList[i])
                queue.append(node.left)
            i += 1
            if i < len(currentList) and currentList[i] != None:
                node.right = TreeNode(currentList[i])
                queue.append(node.right)
            i += 1
        return root
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        data = data[1:-1]
        newList = data.split(', ')
        if newList == ['']:
            return None
        valList = [int(val) if val != "None" else None for val in newList]
        return self.convListToTree(valList)
