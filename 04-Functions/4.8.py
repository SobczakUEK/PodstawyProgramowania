###
# Function that returns time string in 12 or 24 hour format
#
def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"
    else:
        if hours == 0:
            return f"12:{minutes:02d}am"
        elif hours < 12:
            return f"{hours}:{minutes:02d}am"
        elif hours == 12:
            return f"12:{minutes:02d}pm"
        else:
            return f"{hours-12}:{minutes:02d}pm"

# Test cases
print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))
