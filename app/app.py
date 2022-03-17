from asyncio.log import logger
from flask import Flask, render_template, request, redirect
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2, os
import speech_recognition as sr
# from scipy.io.wavfile import write
import scipy
app = Flask(__name__)

@app.route('/')
@app.route('/home')


@app.route('/',methods = ["GET","POST"])
@app.route('/home', methods = ["GET","POST"])

def load_page():
    emotion = ""
    data = request.files["file"]
    if request.method == "POST":

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile()
            data = recognizer.record(audioFile)
            emotion = predict_emotion(data)
    print(emotion)
    return render_template('index.html', data = file)

def predict_emotion(input_audio):
     input=[]
     emotions = {0: 'neutral', 1: 'calm', 2: 'happy', 3: 'sad', 4: 'angry', 5: 'fearful', 6: 'disgust', 7: 'surprised'}
     y, sr = librosa.load(input_audio)
     yt,_ = librosa.effects.trim(y)
     y = yt
     spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=1024, hop_length=100) 
     spectrogram = librosa.power_to_db(spectrogram,ref=np.max)
     librosa.display.specshow(spectrogram, y_axis='mel', fmax=20000, x_axis='time')
     plt.savefig("static/images/image.jpeg")
     image = cv2.imread("static/images/image.jpeg")
     image = cv2.resize(image,(224,224))     # resize image to match model's expected sizing
     image = image.reshape(1,224,224,3) 
     #image = image/255
     #input.append(image)
     new_model = tf.keras.models.load_model('static/models/vgg16_model.h5')
     result = new_model.predict(image)
     y_pred = np.argmax(result,axis=1)
     emotion = emotions[y_pred]
     return emotion

if __name__ == '__main__':
    app.run(debug = True)