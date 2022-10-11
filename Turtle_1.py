import turtle as t 
import math

t.shape("turtle")
t.speed(10)
t.color("blue")

# договор
# дом должен быть посередине участка
walls_width = 300    # ширина стен
walls_height = 100   # высота
door_width = 40      # ширина двери
door_height = 70     # высота двери
roof_height = 150    # высота крыши
roof_side = math.sqrt(roof_height ** 2 + (walls_width / 2) ** 2)         # сторона крыши
roof_angle = math.degrees(math.atan(roof_height / (walls_width / 2)))    # угол крыши

# стены дома
for number in range(2):
	t.fd(walls_width)
	t.left(90)
	t.fd(walls_height)
	t.left(90)

# двери
t.fd(walls_width / 2 - door_width / 2)
for number in range(2):
	t.fd(door_width)
	t.left(90)
	t.fd(door_height)
	t.left(90)

# крыша
t.left(180)
t.fd(walls_width / 2 - door_width / 2)
t.right(90)
t.fd(walls_height)
t.right(90)
t.left(roof_angle)
t.fd(roof_side)
t.right(roof_angle *2)
t.fd(roof_side)

t.done()