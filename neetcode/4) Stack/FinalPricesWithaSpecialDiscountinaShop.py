class Solution:
    def finalPrices(self, prices):
        stack = []
        for i, e in enumerate(prices):
            while stack and prices[stack[-1]] >= e:
                index = stack.pop()
                prices[index] -= e
            stack.append(i)
        return prices



input = "Final Prices With a Special Discount in a Shop"
input2 = "".join(input.split())
print(input2)