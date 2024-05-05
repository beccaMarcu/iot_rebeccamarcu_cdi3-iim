from machine import Pin, PWM 
import network   
import urequests 
import utime 
import ujson 

led = [PWM(Pin(3,mode=Pin.OUT)),PWM(Pin(5,mode=Pin.OUT)),PWM(Pin(7,mode=Pin.OUT))]

for i in led:
    i.freq(1_000)
    i.duty_u16(30000)

maison = {
    "Gryffindor": [0,0,255],
    "Hufflepuff": [255,255,0],
    "Ravenclaw": [255,0,0],
    "Slytherin": [0,255,0]
}

def setColor(c):
    for i in range(3):
        led[i].duty_u16(c[i]*256)


wlan = network.WLAN(network.STA_IF)
wlan.active(True) 
ssid = 'Rebouze'
password = 'Sai7azoh$2020'
wlan.connect(ssid, password) 
url = "http://192.168.0.124:4000/"
while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        r = urequests.get(url) 
        print(r.json()["house"])
        house = r.json()["house"]
        setColor(maison[house])
        r.close()
        utime.sleep(1)
    except Exception as e:
        print(e)