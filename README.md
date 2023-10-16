# HealthGuard
an IOT project for monitoring living environment of elderly people
This code publishes the temperatue data collected by the raspberry Pi Pico W to a mosquitto broker via wifi. 
![image](https://github.com/bishwasshrestha/HealthGuard/assets/29711192/c6e235c5-7ad9-4b8b-a914-b3204a2cf51e)

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
```
rp2.country('FI')

```
mqtt_server = 'xxx.xxx.xxx.xxx' //my mqtt broker(mosquitto) was running on local machine so i put local ip address

client_id = 'PicoW' // device id
```

mqttConnect.py is used to connect pico w via MQTT broker called mosquitto.
select main.py and press run script. Upon running main.py the following should be displayed on your shell. The device is publishing data from a build-in temperature sensor.


![image](https://github.com/bishwasshrestha/HealthGuard/assets/29711192/6d51d9ad-1e25-4bec-8483-d76c031e91ee)
