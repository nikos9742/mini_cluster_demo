import requests
import time
import random

def get_temperature(host, path):
    r = requests.get('http://' + host + '/' + path)
    temp = r.text
    return temp

if __name__ == '__main__':
    while(True):
        temp = get_temperature("localhost:5000", "temp")
        print(temp)
        time.sleep(5)
    