from flask import Flask, render_template, Response
import RPi.GPIO as GPIO
import json as JSON 
import os
from time import sleep
static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')
app = Flask(__name__)
Motor1A = 10
Motor1B = 36
Motor1E = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)


@app.route('/')
def index():
    # GPIO.setmode(GPIO.BOARD)/\
    return render_template('index.html')
    return 'Hi pi loves John and john loves my cakes. we could make cupcakes?'

@app.route('/api/forward')
def forward():
    # GPIO.setmode(GPIO.BOARD)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    return 'Hi mr.Forward'

@app.route('/api/backward')
def backward():
    # GPIO.setmode(GPIO.BOARD)    
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    return 'Hi mr.Backward'

@app.route('/api/halt')
def halt():
    # GPIO.setmode(GPIO.BOARD)    
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.LOW)
    return 'Hi mr.halt'
    
@app.route('/api/pin/<int:pin>')
def lightUpPin(pin):
    # GPIO.setmode(GPIO.BOARD)    
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)
    sleep(5)
    GPIO.output(pin,GPIO.LOW)
    return 'whatever'


@app.route('/api/cleanup')
def cleanup():
    GPIO.cleanup()
    return '{"success":"true", "msg":"Cleanup complete"}'
    

@app.route('/dir/<path:path>', methods=['GET'])
def serve_file_in_dir(path):
 
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')
 
    return send_from_directory(static_file_dir, path)

# RPi.GPIO provides a built-in function GPIO.cleanup() to clean up all the
# ports you've used. But be very clear what this does. It only affects any
# ports you have set in the current program. It resets any ports you have used 
# in this program back to input mode. This prevents damage from, say, a situation
#  where you have a port set HIGH as an output and you accidentally connect it to 
# GND (LOW), which would short-circuit the port and possibly fry it. Inputs can
#  handle either 0V (LOW) or 3.3V (HIGH), so it's safer to leave ports as inputs.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


