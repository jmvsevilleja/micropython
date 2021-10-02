# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
# esp.osdebug(None)
#import webrepl
# webrepl.start()


# import uos, machine
# uos.dupterm(None, 1) # disable REPL on UART(0)
# import gc
# gc.collect()
# test

# import network
# import webcam
# # ESP32 Cam

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.config(dhcp_hostname='esp32cam')

# # SSID and password are stored in flash:
# # micropython code ports/esp32/modnetwork.c was changed to
# # esp_wifi_set_storage(WIFI_STORAGE_FLASH)
# wlan.connect()
# webcam.run()
