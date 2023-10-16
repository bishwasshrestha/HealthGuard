# HealthGuard
## Connect pico w via http 
clone healthguard 
```
clone https://github.com/bishwasshrestha/HealthGuard.git
```
Locate secrets.py file and update ssid and password for wifi connection

```
 secrets={
     'ssid' : 'username',
     'password': 'password'
     }
```

run script on main.py, your shell should print something like this
![image](https://github.com/bishwasshrestha/HealthGuard/assets/29711192/91d2cd5b-57db-490f-8a10-26f147f79d77)

copy the ip address printed above on shell 
open a browser and enter the IP_Address/temp, the browser will display the following html snippet with live temperature update

![image](https://github.com/bishwasshrestha/HealthGuard/assets/29711192/56a462e4-de9e-4f88-94cd-ea7f9c14264e)



