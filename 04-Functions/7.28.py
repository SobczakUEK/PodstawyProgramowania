# def f(dice):
#     max_streak = 0
#     current_streak = 1
#     prev_digit = dice[0]
    
#     for digit in dice[1:]:
#         if digit == prev_digit:
#             current_streak += 1
#             max_streak = max(max_streak, current_streak)
#         else:
#             current_streak = 1
#             prev_digit = digit
    
#     return max_streak

def f(dice):
    countArr = []
    for i in range(1,7):
        countArr.append(dice.count(str(i)))
    
    return countArr.index(max(countArr)) + 1        

print(f("5233165554211"))
print(f("2133"))
