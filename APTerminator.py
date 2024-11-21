"""
  Terminates the ESP32's AP (IT DOES NOT TERMINATE AUTOMATICALLY)
  I recommend running this after you no longer need the esp's AP (espnow doesn't need it to be turned on)
"""
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
ap = network.WLAN(network.AP_IF)
ap.active(False)

while ap.active() == True:
  pass

print('AP Terminated')

