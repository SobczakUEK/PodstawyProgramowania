###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

vol = (a*b*c)
surf = 2*(a*b + b*c + a*c)

print(f'Volume: {vol}')
print(f'Surface area: {surf}')