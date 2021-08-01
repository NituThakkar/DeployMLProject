from flask import Flask,render_template

#initialse the app
app = Flask(__name__)

@app.route('/')
def hello():
        return 'Hello there'
        
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return 'contact page'


if __name__=='__main__':
    app.run()


