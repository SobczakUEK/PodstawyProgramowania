# 24-hour to 12-hour time conversion
time24 = input('Enter time (24-hour format): ')
h, m = time24.split(':')
h = int(h)
ampm = 'am'
if h == 0:
    h12 = 12
elif h == 12:
    h12 = 12
    ampm = 'pm'
elif h > 12:
    h12 = h - 12
    ampm = 'pm'
else:
    h12 = h
print(f'Time in 12-hour format: {h12}:{m}{ampm}')
