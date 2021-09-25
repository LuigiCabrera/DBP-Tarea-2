from flask import Flask
app = Flask(__name__)


@app.route("/<string:name>/<int:d>/<int:m>/<int:y>")
def custom_name(name, d, m, y):

    anios = 2021 - y
    if m > 9: anios += 1
    elif m == 9 and d > 24: anios +=1

    return "Hello " + str(name) + ". You are " +str(anios) + " years old."