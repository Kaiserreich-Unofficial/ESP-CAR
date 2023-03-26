# 导入picoweb模块
import picoweb
import uasyncio as asyncio
from machine import Pin, WDT
from PyCar import PyCar
from HCSR04 import chkdist
from SG90 import Servo

led = Pin(2)
led = Pin(2, Pin.OUT)
# 创建一个picoweb应用对象
app = picoweb.WebApp(__name__)
WirelessCar = PyCar()
wdt = WDT()
# 定义一个视图函数，用于处理网页请求


@app.route("/")
async def index(req, resp):
    # 生成一个HTML页面，包含四个按钮
    html = """
    <html>
    <head>
    <style>
    button {
        width: 100px;
        height: 100px;
        font-size: 20px;
    }
    </style>
    </head>
    <body>
    <h1>Controller</h1>
    <table>
    <tr>
    <td></td>
    <td><button onclick="window.location.href='/Forward'">Forward</button></td>
    <td></td>
    </tr>
    <tr>
    <td><button onclick="window.location.href='/Left'">Left</button></td>
    <td><button onclick="window.location.href='/Stop'">Stop</button></td></td>
    <td><button onclick="window.location.href='/Right'">Right</button></td>
    </tr>
    <tr>
    <td></td>
    <td><button onclick="window.location.href='/Back'">Back</button></td>
    <td></td>
    </tr>
    </table>
    </body>
    </html>
    """

    # 发送HTTP响应头部，指定内容类型为text/html
    await picoweb.start_response(resp, content_type="text/html")

    # 发送HTTP响应主体，即HTML页面
    await resp.awrite(html)

# 定义一个视图函数，用于处理指令请求


@app.route("/Forward")
def forward(req, resp):
    # 调用handle_command函数，传入指令参数
    print("小车前进")
    WirelessCar.forward()
    # 重定向到网页控制器页面
    yield from picoweb.start_response(resp, status="303", headers={"Location": "/"})


@app.route("/Left")
def left(req, resp):
    # 调用handle_command函数，传入指令参数
    print("小车左转")
    WirelessCar.left()
    # 重定向到网页控制器页面
    yield from picoweb.start_response(resp, status="303", headers={"Location": "/"})


@app.route("/Right")
def right(req, resp):
    # 调用handle_command函数，传入指令参数
    print("小车右转")
    WirelessCar.right()
    # 重定向到网页控制器页面
    yield from picoweb.start_response(resp, status="303", headers={"Location": "/"})


@app.route("/Back")
def back(req, resp):
    # 调用handle_command函数，传入指令参数
    print("小车后退")
    WirelessCar.back()
    # 重定向到网页控制器页面
    yield from picoweb.start_response(resp, status="303", headers={"Location": "/"})


@app.route("/Stop")
def stop(req, resp):
    # 调用handle_command函数，传入指令参数
    print("小车刹车")
    WirelessCar.stop()
    # 重定向到网页控制器页面
    yield from picoweb.start_response(resp, status="303", headers={"Location": "/"})


# LED闪烁
async def blink():
    toggle = -1
    while True:
        toggle = toggle * -1
        pin_val = (toggle + 1) * 0.5
        led.value(pin_val)
        wdt.feed()
        await asyncio.sleep(1)


async def radar():
    while True:
        for degree in range(180):
            chkdist()
            Servo(degree)
            print(chkdist(), degree)
            await asyncio.sleep_ms(15)
        for degree in range(180, 0, -1):
            chkdist()
            Servo(degree)
            print(chkdist(), degree)
            await asyncio.sleep_ms(15)

# 将index函数注册为协程视图函数
app.add_url_rule("/", index, coro=True)

# 创建一个事件循环对象
loop = asyncio.get_event_loop()

# 在事件循环中创建一个新任务，执行blink函数
loop.create_task(blink())
loop.create_task(radar())

# 在事件循环中运行picoweb应用对象
loop.run_until_complete(
    app.run(debug=True, port=80, host=ap_if.ifconfig()[0]))
# app.run(debug=True, port=80, host=sta_if.ifconfig()[0])
