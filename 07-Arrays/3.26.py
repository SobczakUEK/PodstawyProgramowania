import matplotlib.pyplot as plt
import math

x = []
y = []

# Create x values (convert degrees to radians)
for degree in range(0, 360):
    x.append(degree)
    y.append(math.sin(math.radians(degree)))

plt.plot(x, y)
plt.grid(True)
plt.show()
