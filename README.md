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

Use Ampy for load script

##### NOTE: You have to use ampy or screen. They cannot be used together otherwise it fails to connect

`ampy --port /dev/ttyUSB0 run blink/blink.py`

