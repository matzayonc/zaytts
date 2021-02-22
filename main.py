from flask import Flask, send_file, request
from gtts import gTTS
import os
from urllib.parse import unquote_plus as decode
from markupsafe import escape


app = Flask(__name__)
static = os.getcwd()+'\\static\\'

counter = 0


def stringToAudioFile(line):
    global counter
    counter += 1
    filename = static + 'tts' + str(counter) + '.mp3'
    tts = gTTS(text=line, lang='en')
    tts.save(filename)
    return filename



@app.route('/')
def hello():
    return "<form method='GET' action='/tts'><input type='text' name='t'><input type='submit'></form>"

@app.route('/tts/<words>')
def tts(words):
    text = decode(words)
    return send_file(stringToAudioFile(text))


@app.route('/tts')
def ttsByArg():
    text = decode(request.args.get('t'))
    return send_file(stringToAudioFile(text))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
