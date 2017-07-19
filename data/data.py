import urllib.request
import time

def sleep(hour,min,sec):
    time.sleep(3600*hour + 60*min + sec)

if __name__ == '__main__':
    while True:
        time.clock()
        url = "http://www.pm25.in/api/querys/pm2_5.json?city=beijing&token=5j1znBVAsnSf5xQyNQyq"
        res = urllib.request.urlopen(url)
        data = res.read()
        data = data.decode('utf-8')
        print(data)
        sleep(1,0,0)
