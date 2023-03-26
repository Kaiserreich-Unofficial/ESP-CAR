from machine import Pin, PWM
# 舵机输出引脚
SG90 = PWM(Pin(2, Pin.OUT))

# 设置pwm频率
SG90.freq(50)


def Servo(n):
    # 公式为c / 180（最大角度） * 2（0°-180°高电平脉冲宽度） + 0.5（舵机角度0°时高电平脉冲宽度）/ 20ms(脉冲周期) * 1023
    ts = int((n / 180 * 2 + 0.5) / 20 * 1023)
    # 输出占空比
    SG90.duty(ts)
