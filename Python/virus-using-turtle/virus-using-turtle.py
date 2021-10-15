# Importing the turtle library
import turtle as trt

# Setting animation parameters
trt.speed(20)
trt.color('yellow')
trt.bgcolor('black')

# Executing animation
i = 200
while i>0:
    trt.left(i)
    trt.forward(i*3)
    i -= 1

trt.done()
# For making sure that the output window does not
# close abruptly when the animation ends.