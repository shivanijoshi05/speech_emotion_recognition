from flask import Flask, render_template, request, redirect
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2, os

app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
@app.route('/home', methods = ["GET","POST"])

def load_page():
    emotion = ""
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            audioFile = 'app/static/demo.wav'
            file.save(audioFile)
            emotion = predict_emotion(audioFile) 
    print(emotion)
    return render_template('index.html')

def predict_emotion(input_audio):
     input = []
     path = "app/static/images/image.jpeg"
     emotions = {0: 'neutral', 1: 'calm', 2: 'happy', 3: 'sad', 4: 'angry', 5: 'fearful', 6: 'disgust', 7: 'surprised'}
     y, sr = librosa.load(input_audio)
     yt,_ = librosa.effects.trim(y)
     y = yt
     spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_fft=1024, hop_length=100) 
     spectrogram = librosa.power_to_db(spectrogram,ref=np.max)
     librosa.display.specshow(spectrogram, y_axis='mel', fmax=20000, x_axis='time')
     plt.savefig(path)
     #image = cv2.imread("app/static/images/image.jpeg")
     #image = cv2.resize(image,(224,224))     # resize image to match model's expected sizing
     image=tf.keras.preprocessing.image.load_img(path, color_mode='rgb', target_size= (224,224))
     image /= 255
     new_model = tf.keras.models.load_model('app/static/models/vgg16_model.h5')
     result = new_model.predict(image)
     y_pred = np.argmax(result,axis=1)
     emotion = emotions[y_pred]
     return emotion

if __name__ == '__main__':
    app.run(debug = True)