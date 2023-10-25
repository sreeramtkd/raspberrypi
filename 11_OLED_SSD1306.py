#Library
#https://pypi.org/project/oled-text/
#icons
#https://fontawesome.com/search?q=wifi&o=r&m=free&f=classic
#VCC=3.3V
#SDA (Physical pin 3)
#SCL (Physical pin 5
#Add cron at reboot @reboot python3 
# DHT11 connected to GPIO04
import time,subprocess,busio,socket
from board import SCL, SDA
from oled_text import OledText, Layout64, BigLine, SmallLine
import Adafruit_DHT as dht
arg_list = [ '/sbin/iwgetid', '-r' ]
args = ' '.join(arg_list)
proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
(output, dummy) = proc.communicate()
print (output)
i2c = busio.I2C(SCL, SDA)
oled = OledText(i2c, 128, 64)
oled.layout = Layout64.layout_icon_only()
oled.text('\uf58b', 1)
time.sleep(2)
oled.layout = Layout64.layout_icon_1big_2small()
oled.text('\uf1eb',1)
oled.text(" "+output, 2)
time.sleep(5)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ipaddr=s.getsockname()[0]
s.close()
oled.layout = Layout64.layout_1big_3small()
oled.text(ipaddr, 1)
time.sleep(10)
oled.layout = Layout64.layout_icon_1big_2small()
while True:
    humidity,temperature = dht.read_retry(dht.DHT11, 4)
    oled.text('\uf769',1)
    oled.text(str(temperature)+" °", 2)
    time.sleep(3)
    oled.text('\uf73d',1)
    oled.text(str(humidity)+" °", 2)
    time.sleep(3)
