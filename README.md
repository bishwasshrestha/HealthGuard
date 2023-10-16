# HealthGuard
an IOT project for monitoring living environment of elderly people
This branch has two additional file oled.py and ssd1306.py(oled driver). 
```
def __init__(self):
        self.i2c = I2C(1, scl=Pin(15), sda=Pin(14))
        self.display = ssd1306.SSD1306_I2C(128, 64, self.i2c)
```

it registers a connected lcd via pin 15 and 14 and displays the temperature recorded from build in temp sensor connected on pin 4

sensor_temp = machine.ADC(4) .

<img src="https://github.com/bishwasshrestha/HealthGuard/assets/29711192/f56bd27e-14ad-420b-bec7-d16ad44cb13e" width="350" height="480">
