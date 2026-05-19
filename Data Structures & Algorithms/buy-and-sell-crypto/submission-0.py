class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrix = [prices[0]]
        maxPrix = [prices[-1]]
        taille = len(prices)
        for i in range(1, len(prices)):
            minPrix.append(min(minPrix[i-1], prices[i]))
            maxPrix.append(max(prices[taille - i - 1], maxPrix[-1]))
        maxPrix = maxPrix[::-1]
        benef = 0
        for i in range(len(prices)):
            achat = maxPrix[i]
            vente = minPrix[i]
            benef = max(benef, achat - vente)
        return benef