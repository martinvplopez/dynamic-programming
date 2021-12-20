# Given an array of positive integers the program start from the first index and every element value will determine the maximum length of possible jump.
# Check whether it is possible to get to the last element.
def jumpGame(numbers):
    goal=len(numbers)-1
    for i in range(len(numbers)-1,-1,-1):
        if i + numbers[i] >= goal:
            goal=i
    return True if goal==0 else False


print(jumpGame([3,2,1,0,5]))