# Function returns array of combinations from the input array to get the best sum represented by targetSum
# If no combination is possible--> return None
# If there are more than 1 best solution -> return any
# Best solution is the one with less numbers

def bestSumClassic(targetSum, numbers):
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    bestCombination = None
    for num in numbers:
        rem = targetSum - num
        result = bestSumClassic(rem, numbers)
        if result is not None:
            combination = result + [num]
            if bestCombination is None or len(combination) < len(bestCombination):
                bestCombination = combination

    return bestCombination


def bestSumMemo(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    bestCombination = None
    for num in numbers:
        rem = targetSum - num
        res = bestSumMemo(rem, numbers)
        if res is not None:
            combination = res + [num]
            if bestCombination is None or len(combination) < len(bestCombination):
                bestCombination = combination
    memo[targetSum] = bestCombination
    return bestCombination


print(bestSumMemo(7, [5, 3, 4, 7]))
print(bestSumMemo(8, [2, 3, 5]))
print(bestSumMemo(8, [1, 4, 5]))
print(bestSumMemo(100, [1, 2, 5, 25]))
