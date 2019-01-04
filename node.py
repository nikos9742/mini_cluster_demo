import random
import requests
import os
import time
import threading
from flask import Flask
app = Flask(__name__)

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
                print(temp)
                time.sleep(1)

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

