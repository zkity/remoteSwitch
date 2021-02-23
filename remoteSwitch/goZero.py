import time
from lib.rotation import Rotation

rot = Rotation(18, 0, 180)

rot.setup()
time.sleep(2)

rot.cleanup()
