# ESP32 micropython

* [Getting Started](http://docs.micropython.org/en/latest/esp32/tutorial/intro.html)
* [Firmware](https://micropython.org/download/esp32/)

### esptool
Using esptool.py you can erase the flash with the command:
```js
esptool.py --port COM14 erase_flash
```
And then deploy the new firmware using:
```js
esptool.py --chip esp32 --port COM14 write_flash -z 0x1000 .\esp32-idf3-20200725-unstable-v1.12-658-gfd2ff867a.bin
```
For ESP8266
```
esptool.py --port COM22 --baud 460800 write_flash --flash_size=detect -fm dio 0 .\esp32-idf3-20200725-unstable-v1.12-658-gfd2ff867a.bin
```

### RSHELL

```js
rshell --port COM14 --baud 115200
```
### VSCODE Tools

* Pymakr Console
*