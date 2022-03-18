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
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

app = Flask(__name__)


@app.route('/',methods = ["GET","POST"])
@app.route('/home', methods = ["GET","POST"])

def load_page():
    emotion = ""
    input_audio = ""
    audioFile = ""
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            input_audio = 'app/static/demo.wav'
            file.save(input_audio)
            emotion = predict_emotion(input_audio) 
    return render_template('index.html', input_audio = input_audio, emotion = emotion)
            audioFile = 'app/static/demo.wav'
            print(audioFile)
            file.save(audioFile)
            emotion = predict_emotion(audioFile) 
            print(emotion)
    return render_template('index.html', emotion=emotion)

def predict_emotion(input_audio):
     path = "app/static/images/image.jpeg"
     emotions = {0: 'Neutral', 1: 'Calm', 2: 'Happy', 3: 'Sad', 4: 'Angry', 5: 'Fearful', 6: 'Disgust', 7: 'Surprised'}
     y, sr = librosa.load(input_audio)
     yt,_ = librosa.effects.trim(y)
     y = yt
     spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=1024, hop_length=100) 
     spectrogram = librosa.power_to_db(spectrogram,ref=np.max)
     librosa.display.specshow(spectrogram, y_axis='mel', fmax=20000, x_axis='time')
     plt.savefig(path)
     #image = cv2.imread("app/static/images/image.jpeg")
     #image = cv2.resize(image,(224,224))     # resize image to match model's expected sizing
     image = tf.keras.preprocessing.image.load_img(path, color_mode='rgb', target_size= (224,224))
     # image /= 255
     image = load_image(path)
     new_model = tf.keras.models.load_model('app/static/models/vgg16_model.h5')
     result = new_model.predict(image)
     y_pred = int(np.argmax(result, axis=1))
     emotion = emotions[y_pred]
     return emotion 
 
def load_image(img_path):
    image = load_img(img_path, target_size=(224, 224))
    image = img_to_array(image)
    image = image.reshape((image.shape[0], image.shape[1], image.shape[2]))           
    img_tensor = np.expand_dims(image, axis=0)       
    img_tensor /= 255.                                     
    return img_tensor

if __name__ == '__main__':
    app.run(debug = True)