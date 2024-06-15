from m5stack import *
from m5ui import *
from uiflow import *
import machine
import time
import unit
remoteInit()
import machine

pir_0 = unit.get(unit.PIR, (0,22))

switch_value = None
rp_gauge2_data = None

def gauge_2_callback():
  global rp_gauge2_data, switch_value, pin0, pir_0 
  return rp_gauge2_data
def switch_RUHE_callback(switch_value):
  global rp_gauge2_data, pin0, pir_0 
  print(switch_value)

pin0 = machine.Pin(26, mode=machine.Pin.OUT, pull=machine.Pin.PULL_UP)
switch_value = 0
rgb.setColorAll(0x000000)
while True:
  if switch_value != 1:
    if (pir_0.state) == 1:
      print('PIR Status: Detected')
      pin0.on()
      rgb.setColorAll(0xff0000)
      rp_gauge2_data = 100
    else:
      pin0.off()
      rgb.setColorAll(0x000000)
      rp_gauge2_data = 0
    wait_ms(500)
  else:
    pin0.off()
  wait_ms(2)
