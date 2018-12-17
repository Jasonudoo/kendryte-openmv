import image
import sensor


face_cascade = image.HaarCascade("frontalface", stages=100)
print(face_cascade)
while (True):
    img = sensor.snapshot()
    objects = img.find_features(face_cascade, threshold=1.00, scale=1.1)
    for r in objects:
        img.draw_rectangle(r, color=(0, 255, 255))
        print(r)
    nop = img.show()
