from machine import I2C
import utime

# 初始化I2C 按需改引脚和通道
i2c = I2C(I2C.I2C0, I2C.STANDARD_MODE)

# IIC超声波默认地址
SONAR_ADDR = 0x57

def iic_ultrasonic_read():
    # 读取2字节距离数据
    try:
        data = i2c.read(SONAR_ADDR, 0x00, 2)
    except Exception:
        return None
    
    # 合成数值 单位:mm
    distance_mm = (data[0] << 8) | data[1]
    # 转成 cm
    distance_cm = distance_mm / 10.0
    return round(distance_cm, 2)

while True:
    dist = iic_ultrasonic_read()
    if dist is None:
        print("IIC读取失败")
    else:
        print("距离：", dist, "cm")
    utime.sleep(0.2)