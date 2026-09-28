import time
import board

from adafruit_bme280 import basic
from src.gui import createGui

i2c = board.I2C()

bme280 = basic.Adafruit_BME280_I2C(
    i2c,
    address=0x77 #I2C adress of BME280 sensor
)

createGui(bme280)