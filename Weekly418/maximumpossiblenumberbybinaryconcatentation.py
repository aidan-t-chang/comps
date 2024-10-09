class Solution:
    def maxGoodNumber(self, nums) -> int:
        b = [bin(num)[2:] for num in nums]
        test = []
        one = b[0] + b[1] + b[2]
        two = b[1] + b[2] + b[0]
        three = b[2] + b[0] + b[1]
        four = b[2] + b[1] + b[0]
        five = b[1] + b[0] + b[2]
        six = b[0] + b[2] + b[1]
        test.append(one)
        test.append(two)
        test.append(three)
        test.append(four)
        test.append(five)
        test.append(six)
        res = float('-inf')

        for t in test:
            res = max(res, int(t, 2))
        return res