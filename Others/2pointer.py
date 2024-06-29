class Solution:
    def twoSum(self, numbers: list[int], target: int):
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return f"L: {numbers[l]}\nR: {numbers[r]}"
            elif sum < target:
                l += 1
            else:
                r -= 1

            if l == r:
                return None
        if None:
            print("No solution found")


x = Solution()
print(x.twoSum([2,7,11,15], 9))
