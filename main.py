from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi pi loves John and john loves my cakes. we could make cupcakes?'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')