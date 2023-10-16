import machine
import utime
led = machine.Pin('LED', machine.Pin.OUT)
led.on()
#reading temperature from a sensor
sensor_temp = machine.ADC(4)
#max voltage of pico is 3.3 and max value of ADC is 65535
conversion_factor = 3.3/65535
index=1
while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27-(reading -0.706)/0.001721
    print(index,' raw data reading :', reading, ' temperature:', temperature)
    index+=1
    utime.sleep(5)
potentiometer = machine.ADC(26)
while True:
    voltage = potentiometer.read_u16()*conversion_factor
    print('voltage:',voltage)
    utime.sleep(2)