###
# A program that prints your height both in cm and in feet and inches.
#

# 1ft = 30.48cm
# 1in = 2.54cm

# could've done it better, but don't know if it's allowed to change already present code

cm = 170
# Use the division operator without remainder
feet = int(cm // 30.48)
# The operator calculating the remainder of the division
inches = (cm * 0.3937) % 12
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')