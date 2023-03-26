from machine import Pin, PWM


class PyCar():
    def __init__(self, pin1=5, pin2=4, pin3=12, pin4=13):
        self.pwm1 = self.set_pin(pin1)
        self.pwm2 = self.set_pin(pin2)
        self.pwm3 = self.set_pin(pin3)
        self.pwm4 = self.set_pin(pin4)

    def set_pin(self, n):
        return PWM(Pin(n), freq=50)

    def forward(self):
        self.pwm1.duty(900)
        self.pwm2.duty(0)
        self.pwm3.duty(900)
        self.pwm4.duty(0)

    def back(self):
        self.pwm1.duty(0)
        self.pwm2.duty(900)
        self.pwm3.duty(0)
        self.pwm4.duty(900)

    def left(self):
        self.pwm1.duty(900)
        self.pwm2.duty(0)
        self.pwm3.duty(0)
        self.pwm4.duty(900)

    def right(self):
        self.pwm1.duty(0)
        self.pwm2.duty(900)
        self.pwm3.duty(900)
        self.pwm4.duty(0)

    def stop(self):
        self.pwm1.duty(0)
        self.pwm2.duty(0)
        self.pwm3.duty(0)
        self.pwm4.duty(0)
