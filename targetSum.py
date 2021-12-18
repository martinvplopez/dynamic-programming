# Given an array of numbers and a target integer, count the total ways you can add the numbers to get the target
# Example: [1,1,1,1] target=3 output should be 4 because:
# -1 + 1 + 1 +1
# +1 -1 +1 +1 and so on

def targetSum(numbers, target):
    memo={}
    def t(i, total):
        if i==len(numbers):
            return 1 if total==0 else 0
        if (i,total) in memo:
            return memo[(i,total)]
        memo[(i,total)]= t(i+1,total+numbers[i]) + t(i+1,total-numbers[i])
        return memo[(i,total)]
    return t(0,target)

print(targetSum([1,1,1,1,1],3))