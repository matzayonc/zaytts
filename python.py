from gtts import gTTS
my_tts = "przyganiał kocioł garnkowi"
tts = gTTS(text=my_tts, lang='en')
tts.save("C:/Users/mateo/Desktop/file.mp3")

