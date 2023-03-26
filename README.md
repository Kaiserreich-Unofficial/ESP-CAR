# ESP-CAR

一个简易的Wifi避障小车，采用ESP8266方案

### 需要的设备

ESP8266核心板、HCSR04超声测距模块、SG90舵机、小车底盘（130电机）、18650电池若干

### 平台

micropython == 1.19.1

micropython-ulogging == 0.3

picoweb == 1.8.2

***注：micropython采用乐鑫官网flash_tools刷入，方法详见百度。ulogging和picoweb均使用upip安装，如果不会使用upip可以在PC部署好python环境后安装thonny编辑器并使用其"管理包"功能安装扩展库。安装目录在ESP8266的"\/lib"目录下。***
