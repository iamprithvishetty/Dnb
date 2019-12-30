import spidev
import os
import time
from pymouse import PyMouse
push=1
counter = 0
m=PyMouse()
max_v=12
centre=max_v/2
threshold=max_v/4
j=m.position()[0]
k=m.position()[1]
spi = spidev.SpiDev()
spi.open(0,0)
swt_channel = 0
vrx_channel = 1
vry_channel = 2
delay = 0.5
def ReadChannel(channel):
    adc=spi.xfer2([1,(8+channel)<<4,0])
    data=((adc[1]&3)<<8)+adc[2]
    return data

def C_value(this_value,centre):
  reading = this_value*max_v/1024
  center=centre
  distance = reading - center
  if abs(distance) < threshold: 
   distance = 0
  return distance


while True:
    try:
        x=ReadChannel(vrx_channel)
        y=ReadChannel(vry_channel)
        push=ReadChannel(swt_channel)
        x_max = m.screen_size()[0]
        y_max = m.screen_size()[1]
        print(x,y)
        x_new= C_value(x,centre)
        y_new= C_value(y,centre)
        m.move(j+x_new,k-y_new)
        j=m.position()[0]
        k=m.position()[1]
        if push==0:
            counter = 1
        if counter-push == 0:
            m.click(j+x_new,k-y_new,1)
            counter = 0
        time.sleep(delay)
    except IndexError:
        print('Error occured');
 
 