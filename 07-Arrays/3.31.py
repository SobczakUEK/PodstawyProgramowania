array = [[-38, 19], [5,40], [-7,11], [29,16]]
min_val = array[0][0]
max_val = array[0][0]
min_row = min_col = max_row = max_col = 0

for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] < min_val:
            min_val = array[i][j]
            min_row = i
            min_col = j
        if array[i][j] > max_val:
            max_val = array[i][j]
            max_row = i
            max_col = j

print(f"Smallest value {min_val} is at row {min_row+1}, column {min_col+1}")
print(f"Largest value {max_val} is at row {max_row+1}, column {max_col+1}")
