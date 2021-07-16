#!/usr/bin/python

from Adafruit_BMP085 import BMP085
import time
import datetime
import board
from datetime import datetime




# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)

# To specify a different operating mode, uncomment one of the following:
# bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
# bmp = BMP085(0x77, 1)  # STANDARD Mode
# bmp = BMP085(0x77, 2)  # HIRES Mode
# bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

while True:
    temp = bmp.readTemperature()

    # Read the current barometric pressure level
    pressure = bmp.readPressure()

    # To calculate altitude based on an estimated mean sea level pressure
    # (1013.25 hPa) call the function as follows, but this won't be very accurate
    altitude = bmp.readAltitude()

    # To specify a more accurate altitude, enter the correct mean sea level
    # pressure level.  For example, if the current pressure level is 1023.50 hPa
    # enter 102350 since we include two decimal places in the integer value
    # altitude = bmp.readAltitude(102350)
    f = open("rezultate_bmp.txt","a")
    with open("rezultate_bmp.txt","a",encoding = "utf8") as f:
        now = datetime.now()
        f.write("Temperature: %.2f C\n" % temp)
        f.write("Pressure:    %.2f hPa \n" % (pressure / 100.0))
        f.write("Altitude:    %.2f \n" % altitude)
        f.write("data : " + str(now.strftime("%d/%m/%Y, %H:%M:%S")) + "\n")
    time.sleep(600.0)
    f.close()



