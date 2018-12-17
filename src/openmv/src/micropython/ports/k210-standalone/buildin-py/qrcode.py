import image
import sensor

while(True):
    img = sensor.snapshot()
    for code in img.find_qrcodes():
        img.draw_rectangle(code.rect(), color=(255, 0, 0))
        img.draw_string(10, 10, code.payload(), color=(
            0, 255, 255), scale=3, mono_space=False)
        print(code)
    img.show()
