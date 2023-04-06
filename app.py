from flask import Flask

UPLOAD_FOLDER = 'C:/Users/hp/Desktop/Flask/keras_imagenet/uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER