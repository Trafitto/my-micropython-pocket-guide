# My pocket guide to Mictopython on ESP8266 Nodemcu V3

Just a collection of things I am learning while trying and using micropython

## Installations

I dunno why but I cannot flash the Micropython firmware on Ubuntu due to an esptool error (connection failed).

So I follow the tutorial step with my Windows PC and everything works fine

In the new releases of Micropython it is necessary to set a password to access the webRel, I configured it with screen.

## Dependencies

- Ampy

    `pip install adafruit-ampy`

## Usage

Connect to RELP (Read Evaluate Print Loop) with screen

`screen /dev/ttyUSB0 115200` 

RELP is basically an onboard python console

Use Ampy for run script

##### NOTE: You have to use ampy or screen. They cannot be used together otherwise it fails to connect

`ampy --port /dev/ttyUSB0 run blink/blink.py`

Permanently run the script (Also: Run on boot)

`ampy --port /dev/ttyUSB0 put blink/blink.py /main.py`


## Networking

Connect the NodeMcu to your wifi

Just follow [this steps](https://docs.micropython.org/en/latest/esp8266/quickref.html#networking)

Leave this functions here Micropython says it's useful... I have no idea

```
def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('essid', 'password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
```


## Installing package

You can install package with your RELP (with screen)

Import upip:

```
import upip
upip.install('urequests')
```

