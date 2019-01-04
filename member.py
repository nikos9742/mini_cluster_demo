import random
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Member"

@app.route("/temp")
def get_temp():
    temp = random.randint(17, 25)
    
    return "" + str(temp)

if __name__ == "__main__":
    app.run()
