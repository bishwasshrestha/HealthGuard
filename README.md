# HealthGuard
an IOT project for monitoring living environment of elderly people
This code publishes the temperatue data collected by the raspberry Pi Pico W to a mosquitto broker via wifi. 
![image](https://github.com/bishwasshrestha/HealthGuard/assets/29711192/c6e235c5-7ad9-4b8b-a914-b3204a2cf51e)

Update the code as mentioned below and device will publishing data from a built-in temperature sensor.
![image](https://github.com/bishwasshrestha/HealthGuard/assets/29711192/de501690-4a28-4e37-a406-1157b2867266)

clone the repo
``` 
git clone https://github.com/bishwasshrestha/HealthGuard.git
```
setup and connect your Pico W to your machine

Upload the cloned files to the pico W 

Find 'Secrets.py' file and add ssid and password to the network preferred
```
secrets={
    'ssid' : 'username',
    'password': 'password'
    }
```
If you are outside Finland please locate wifi.py file and update the location to your location in init_wifi() method.

rp2.country('FI')

```
mqtt_server = 'xxx.xxx.xxx.xxx' //my mqtt broker(mosquitto) was running on local machine so i put local ip address

client_id = 'PicoW' // device id
```

mqttConnect.py helps to connect pico w via MQTT broker called mosquitto.


