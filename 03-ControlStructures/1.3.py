# Checking whether a car exceeded the speed limit
speed_limit = 140
try:
    car_speed = int(input('Enter car speed (km/h): '))
except ValueError:
    print('Invalid input')
else:
    if car_speed > speed_limit:
        print(f'Your speed is {car_speed}km/h')
        print('Warning: speed limit exceeded!!')
    else:
        print(f'Your speed is {car_speed}km/h')
        print('OK')
