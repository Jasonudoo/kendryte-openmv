import image
import sensor

while(True):
    img = sensor.snapshot()
    img = img.draw_string(
        20, 20, "OpenMV Base on MaixPy @kendryte K210", scale=2)
    nop = img.show()
