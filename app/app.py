from flask import Flask,  render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


if _name_ == "__main__":
    app.run(debug=True)