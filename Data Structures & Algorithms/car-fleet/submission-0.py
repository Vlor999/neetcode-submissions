class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []

        taille = len(position)
        for i in range(taille) :
            pair.append((position[i], speed[i]))
        
        pair = sorted(pair, reverse=True)
        for pos, vit in pair:
            tps = (target - pos) / vit
            stack.append(tps)
            if len(stack) >= 2 and tps <= stack[-2]:
                stack.pop()
        return len(stack)        