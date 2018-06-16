from flask import Flask
import RPi.GPIO as GPIO
from time import sleep
app = Flask(__name__)
Motor1A = 16
Motor1B = 15
Motor1E = 22
GPIO.setmode(GPIO.BOARD)

@app.route('/')
def index():
    GPIO.setmode(GPIO.BOARD)
    return 'Hi pi loves John and john loves my cakes. we could make cupcakes?'

@app.route('/api/forward')
def forward():
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    return 'Hi mr.Forward'

@app.route('/api/backward')
def backward():
    GPIO.setmode(GPIO.BOARD)    
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    return 'Hi mr.Backward'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


