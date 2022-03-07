from flask import Flask, render_template
import numpy as np
import pickle
app = Flask(__name__)
cd c
@app.route('/')
@app.route('/home')
def load_page():
     return render_template('index.html')

def ValuePredictor(input_audio):
    to_predict = np.array(input_audio).reshape(1, 12)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

if __name__ == '__main__':
    app.run(debug = True)