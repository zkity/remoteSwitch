import time
from lib.rotation import Rotation

rot = Rotation(18, 0, 180)

rot.setup()
time.sleep(2)

ang = 100
for i in range(0, ang):
    rot.positiveRotation()
time.sleep(0.5)
for i in range(0, ang):
    rot.reverseRotation()

rot.cleanup()
