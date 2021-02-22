from flask import Flask, send_file
from gtts import gTTS
import os

from markupsafe import escape
app = Flask(__name__)
static = os.getcwd()+'\\static\\'

counter = 0


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/tts/<words>')
def tts(words):
    global counter
    tts = gTTS(text=words, lang='en')
    counter += 1
    filename = static + 'tts' + str(counter) + '.mp3'
    print(filename)
    tts.save(filename)
    return send_file(filename)

if __name__ == '__main__':
    app.run()
