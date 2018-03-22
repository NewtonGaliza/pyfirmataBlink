from pyfirmata import Arduino, util

import time

board = Arduino('/dev/tty/USB0')
for i in range(10):
              board.digital[13].write(1)
               time.sleep(1)
               board.digital[13].write(0)
               time.sleep(1)
