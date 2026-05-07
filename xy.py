#adc0 --y轴
#adc1 --x轴
#gpio31 --key

from machine import  Pin
from misc import ADC
import utime

y=ADC()
x=ADC()

# 简单主循环：读取 ADC 并打印
try:
    while True:
        x1 = x.read(ADC.ADC0)
        y1 = y.read(ADC.ADC1)
        print("X_raw: {}  Y_raw: {}".format(x1, y1))
        utime.sleep_ms(200)
except KeyboardInterrupt:
    print("退出")
# ...existing code...