import random
import requests
import os
import time
import threading
import math
from flask import Flask
app = Flask(__name__)


# Reccurent task
@app.before_first_request
def activate_job():
    def run_job():
        while True:
            print("Run recurring task")
            time.sleep(3)
            HEAD_STATUS = os.getenv('HEAD_STATUS', default='False')
            print(HEAD_STATUS)
            if HEAD_STATUS == "True":
                # export HEAD_STATUS=True
                # unset HEAD_STATUS
                temp = get_temperature("localhost:5000", "temp")
                print("Self temp")
                print(temp)
                time.sleep(1)
                try:
                    temp1 = get_temperature("node1:5000", "temp")
                    temp2 = get_temperature("node2:5000", "temp")
                    temp3 = get_temperature("node3:5000", "temp")
                    temp4 = get_temperature("node4:5000", "temp")
                    print("Node temps" + temp1 + temp2 + temp3 + temp4)
                    print((temp1 + temp2 + temp3 + temp4) / 4)
                except:
                    print('Failed to get temp on all 4 nodes')                    
                print(temp)

    thread = threading.Thread(target=run_job)
    thread.start()

def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            print('In start loop')
            try:
                r = requests.get('http://127.0.0.1:5000/')
                if r.status_code == 200:
                    print('Server started, quiting start_loop')
                    not_started = False
                print(r.status_code)
            except:
                print('Server not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()

def get_temperature(host, path):
    r = requests.get('http://' + host + '/' + path)
    temp = r.text
    return temp

@app.route("/")
def hello():
    return "Member"

@app.route("/temp")
def get_temp():
    temp = random.randint(17, 25)
    
    return "" + str(temp)

if __name__ == "__main__":
    start_runner()
    app.run()

