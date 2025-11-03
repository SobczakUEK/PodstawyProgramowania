from figures import *


mult = 100
offset1 = -120
offset2 = 120
for i in range(2):
    move_turtle(offset1 + i*mult, offset1 + i*mult)
    draw_square(50)
    move_turtle(i*mult, i*mult)
    draw_trangle(50)
    move_turtle(offset2 + i*mult, offset2 + i*mult)
    draw_rectangle(20, 60)

end()