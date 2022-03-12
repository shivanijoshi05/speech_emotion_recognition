from flask import Flask, render_template, request, redirect
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
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
            emotion = predict_emotion(file)
    print(emotion)
    return render_template('index.html')

def predict_emotion(input_audio):
     input=[]
     emotions = {0: 'angry', 1: 'calm', 2: 'disgust', 3: 'fearful', 4: 'happy', 5: 'neutral', 6: 'sad', 7: 'surprised'}
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
     result = new_model.predict(input)
     y_pred = np.argmax(result,axis=1)
     emotion = emotions[y_pred]
     return emotion

if __name__ == '__main__':
    app.run(debug = True)